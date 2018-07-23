# -*- coding: utf-8 -*-
import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(__file__)) + "\\..\\")
import pika
import json
import arrow
import threading
import queue
from loach.constant import Task, Stat
from loach.utils.exception import DeviceTimeoutException
from loach.utils import retry
from loach.devicemanager import DeviceManager, Device
from loach.command import DouYinCommand


class Schedule(threading.Thread):
    def __init__(self, device_manager):
        super().__init__()
        # 任务命令的队列
        self._queue = queue.Queue(maxsize=100)
        # 控制命令的队列
        self._ctl_queue = queue.Queue(maxsize=10)
        self.device_manager = device_manager

    def run(self):
        threading.Thread(target=self.ctl_listener).start()
        while True:
            if self._queue:
                cmd = self._queue.get(block=True)
                try:
                    self.excute(cmd)
                except DeviceTimeoutException as e:
                    print("DeviceTimeoutException")
                    import traceback
                    traceback.print_exc()

    # 子线程抛出的异常捕捉不到，所以这里的无限重试只作用于本线程的异常
    @retry(forever=True)
    def excute(self, command, times=None):
        timeout = command['timeout']
        s = arrow.now().timestamp
        e = s + timeout if timeout else 0
        while not timeout or s <= e:
            device = self.device_manager.get_device_prepared()
            if not device and command['force']:
                device = self.device_manager.get_device_running(Task.CRAWLING)
            if device:
                break
            else:
                s = arrow.now().timestamp
        else:
            raise DeviceTimeoutException(msg="没有可用的设备，正在等待设备就绪。。。")
        try:
            t = threading.Thread(target=device.do, args=(command, device.udid))
            t.start()
        except Exception as e:
            if device:
                device.modify_stat(Stat.RUNNING)
            import traceback
            traceback.print_exc()
            raise e

    def ctl_listener(self):
        while True:
            if self._ctl_queue:
                cmd = self._ctl_queue.get(block=True)
                if cmd['task_type'] == Task.ADD_DEVICE:
                    self.device_manager.add_device(Device(**(cmd['data'])))

    def push_command(self, command):
        print('收到命令', command)
        if command['task_type'] == Task.ADD_DEVICE:
            self._ctl_queue.put(command)
        else:
            self._queue.put(command)


def int2menu(t):
    if t == 1:
        return Task.FINDING
    if t == 2:
        return Task.CRAWLING
    if t == 4:
        return Task.ADD_DEVICE


dm = DeviceManager()
schedul = Schedule(dm)


def main():
    print("11111111")
    devices = []
    device = ("127.0.0.1", 62025, "192.168.1.177", 4723)
    devices.append(device)
    # device = ("127.0.0.1", 62026, "192.168.1.3", 4723)
    # devices.append(device)
    dm = DeviceManager(devices)
    schedul = Schedule(dm)
    schedul.start()
    schedul.push_command(DouYinCommand(**{"task_type": Task.FINDING, "data":{"short_id":"kelly0711","attrs": ["following", "work", "like"]}}))
    def cb(ch, method, properties, body):
        data = json.loads(body.decode('utf-8'))
        data['task_type'] = int2menu(data['task_type'])
        print('收到命令', data)
        schedul.push_command(DouYinCommand(**data))

        ch.basic_ack(delivery_tag=method.delivery_tag)

    con = pika.BlockingConnection(pika.ConnectionParameters(host='', port=5672, virtual_host='/',
                                                            credentials=pika.PlainCredentials('',
                                                                                              '')))
    channel = con.channel()

    channel.basic_consume(cb, queue="douyin.task.cmd")

    channel.start_consuming()


if __name__ == "__main__":
    main()

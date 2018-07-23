# -*- coding: utf-8 -*-
import json
from loach.api import douyin
from loach.command import DouYinCommand
from loach.constant import Task
from loach.instances.pikaapp import send_task
from loach.schedule import schedul
from flask import request
import json


@douyin.route('/hello/', methods=['GET'])
def hello():
    return 'hello'


@douyin.route('/task/search/', methods=['POST'])
def task_search():
    cmd = DouYinCommand(task_type=Task.FINDING, data=json.loads(request.data))
    # send_task(cmd)
    schedul.push_command(cmd)
    return cmd.__str__()


@douyin.route('/task/crawling/', methods=['POST'])
def task_crawling():
    cmd = DouYinCommand(task_type=Task.CRAWLING, data=json.loads(request.data))
    # send_task(cmd)
    schedul.push_command(cmd)
    return cmd.__str__()


@douyin.route('/task/device/', methods=['POST'])
def task_device_add():
    cmd = DouYinCommand(task_type=Task.FINDING.ADD_DEVICE, data=json.loads(request.data))
    # send_task(cmd)
    schedul.push_command(cmd)
    return cmd.__str__()


@douyin.route('/task/devices/', methods=['POST'])
def task_devices_add():
    cmds = json.loads(request.data)
    for cmd in cmds.values():
        cmd = DouYinCommand(task_type=Task.FINDING.ADD_DEVICE, data=cmd)
        # send_task(cmd)
        schedul.push_command(cmd)
    return cmd.__str__()

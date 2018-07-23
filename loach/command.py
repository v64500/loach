# -*- coding: utf-8 -*-

# cmd = {
#     'app_name': 'douyin',
#     'task_type': Task.FINDING,
#     'force': False,
#     'timeout': 30 等待可用设备的时间
#     'data': {
#     }
# }
from collections import Iterable
from loach.constant import Task
from loach.utils.exception import CommandInvalidException


class Command(object):
    def __init__(self, **kwargs):
        self.cmd = kwargs
        if "app_name" not in self.cmd.keys():
            raise CommandInvalidException(msg="缺少属性 app_name")
        if "task_type" not in self.cmd.keys():
            raise CommandInvalidException(msg="缺少属性 task_type")
        if "timeout" not in self.cmd.keys():
            self.cmd['timeout'] = None
        if "force" not in self.cmd.keys():
            self.cmd['force'] = False
        if self.cmd['task_type'] == Task.CRAWLING and self.cmd['force']:
            raise CommandInvalidException(msg="CRAWLING任务不允许设置force为True")
        if "data" not in self.cmd.keys():
            raise CommandInvalidException(msg="缺少属性 data， 必须指定data属性")

    @property
    def app_name(self):
        return self.cmd["app_name"]

    def __getitem__(self, item):
        return self.cmd[item]

    def __str__(self):
        return self.cmd.__str__()

    def __repr__(self):
        return self.__str__()


class DouYinCommand(Command):
    def __init__(self, **kwargs):
        if not kwargs.get('app_name'):
            kwargs['app_name'] = 'douyin'
        super().__init__(**kwargs)
        if self.cmd['task_type'] == Task.CRAWLING:
            if 'attrs' not in self.cmd['data'].keys():
                self.cmd['data']['attrs'] = None
            elif not isinstance(self.cmd['data']['attrs'], Iterable):
                raise CommandInvalidException('data.attrs必须是可迭代类型')
        if self.cmd['task_type'] == Task.FINDING:
            if 'short_id' not in self.cmd['data'].keys():
                raise CommandInvalidException('抖音搜索任务必须指定 short_id')
            if 'attrs' not in self.cmd['data'].keys():
                self.cmd['data']['attrs'] = None
            elif not isinstance(self.cmd['data']['attrs'], Iterable):
                raise CommandInvalidException('data.attrs必须是可迭代类型')
        if self.cmd['task_type'] == Task.ADD_DEVICE:
            if 'ip' not in self.cmd['data'].keys() or 'port' not in self.cmd['data'].keys() or 'sip' not in self.cmd['data'].keys() or 'sport' not in self.cmd['data'].keys():
                raise CommandInvalidException('必须指定要添加的设备的信息')

    def is_force(self):
        return self.cmd['force']
# -*- coding: utf-8 -*-

from enum import Enum


class Stat(Enum):
    # 就绪态 没有执行任何app
    PREPARED = 1
    # 运行态 正在运行app
    RUNNING = 2
    # 错误态
    FAULT = 4
    # 设备断开连接（模拟器进程死亡）
    NOT_FOUND = 8


class Task(Enum):
    FINDING = 1
    CRAWLING = 2
    ADD_DEVICE = 4


class Extra(Enum):
    FORCE = 1
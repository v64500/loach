# -*- coding: utf-8 -*-
from appium.common.exceptions import NoSuchContextException
from selenium.common.exceptions import *
from urllib.error import URLError


class DouYinTimeoutException(TimeoutException):
    pass


class DeviceTimeoutException(TimeoutException):
    pass


class DouYinElementException(NoSuchElementException):
    pass


class AppNotFoundException(Exception):
    pass


class DouYinFindTaskFailed(Exception):
    def __init__(self, msg):
        self.msg = msg
    pass


class DouYinUnknowException(Exception):
    def __init__(self, msg):
        self.msg = msg
    pass


class AppiumServerTimeout(URLError):
    def __init__(self, msg=None):
        super().__init__(msg)
        self.msg = msg

    def __str__(self):
        return '<urlopen error %s>' % self.msg


class DeviceError(WebDriverException):
    pass


class CommandInvalidException(Exception):
    pass
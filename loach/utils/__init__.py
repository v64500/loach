# -*- coding: utf-8 -*-
import time
from functools import wraps


def retry(times=3, forever=False):
    def decorate(func):
        @wraps(func)
        def retryed(*args, **kwargs):
            i = 0
            while forever or i < times+1:
                try:
                    return func(*args, times=i, **kwargs)
                except Exception as e:
                    i = i + 1
                    print(e)
                    print("第 %d 次重试。[msg]: %s" % (i, e.msg))
                    time.sleep(1)
                    import traceback
                    traceback.print_exc()

        return retryed
    return decorate

# -*- coding: utf-8 -*-

import subprocess


class AppiumServer(object):
    def __init__(self):
        pass

    def start(self, servers):
        """
        a list of tuple,  (port, bootstrap-port, udid)
        :param servers:
        """
        for p, bp, udid in servers:
            # cmd = "appium -p %d -bp %d -U %s" % (p, bp, udid)
            r = subprocess.run(["appium", "-p", str(p), "-bp", str(bp), "-U", udid])

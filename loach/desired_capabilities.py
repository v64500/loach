import os

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


def get_desired_capabilities(app=None, platform=None, device_name=None):
    desired_caps = {
        "platformName": "Android",
        "automationName": "Appium",
        # "Emulator"\"SLA-AL00",
        "deviceName": device_name,
        # "app": "I:\\pywork\\dolphin\\opt\\%s" % app,
        "platformVersion": platform,
        "appPackage": "com.ss.android.ugc.aweme",
        "appActivity": "com.ss.android.ugc.aweme.main.MainActivity",
        "noReset": True
    }
    if app:
        desired_caps["app"] = app

    return desired_caps
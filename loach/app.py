# -*- coding: utf-8 -*-
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.touch_action import TouchAction


# the emulator is sometimes slow and needs time to think
SLEEPY_TIME = 1


class App(object):

    def __init__(self, desired_caps, sip, sport):
        self.driver = webdriver.Remote('http://%s:%d/wd/hub' % (sip, sport), desired_caps)
        self.wait = WebDriverWait(self.driver, 30)
        # {'width':w, 'height':h}
        self.window = self.driver.get_window_size()

    def set_up(self):
        id = self.driver.session_id
        print(id)

    def tear_down(self):
        self.driver.quit()

    def wait_element_clickable(self, locator):
        return self.wait.until(
            EC.element_to_be_clickable(locator)
        )

    def back(self):
        self.driver.back()

    def center(self, left_top, right_bottom):
        x = (left_top[0] + right_bottom[0]) / 2
        y = (left_top[1] + right_bottom[1]) / 2
        return x, y

    def click_by_xy(self, left_top, right_bottom):
        location = self.center(left_top, right_bottom)
        self.driver.tap([location], 200)

    def swip(self, x1, y1, x2, y2, duration=None):
        action = TouchAction(self.driver)
        action.press(x=x1, y=y1) \
            .wait(300) \
            .move_to(x=x2, y=y2) \
            .release() \
            .perform()

    def app_is_installed(self, app_package):
        self.driver.is_app_installed(app_package)

    @property
    def page_source(self):
        return self.driver.page_source

    def quit(self):
        self.driver.quit()


if '__main__' == __name__:
    t = App()




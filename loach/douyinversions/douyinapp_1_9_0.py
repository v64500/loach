# -*- coding: utf-8 -*-
import time
from loach.app import App
from loach.desired_capabilities import get_desired_capabilities
from loach.constant import Task, Stat
from loach.utils import retry
from appium.webdriver.common.mobileby import MobileBy as By
from selenium.common.exceptions import (TimeoutException,
                                        NoSuchElementException,
                                        WebDriverException)
from loach.utils.exception import (DouYinFindTaskFailed)
from selenium.webdriver.support.ui import WebDriverWait
from appium.webdriver.common.touch_action import TouchAction
from loach.appbuttonmanager import AppButtonManager


class Button(object):
    def __init__(self, left_top=None, right_bottom=None, id=None, name=None, text=None, locator=None):
        self.left_top = left_top
        self.right_bottom = right_bottom
        self.id = id
        self.name = name
        self.text = text
        self.locator = locator
        # self.uiselector = uiselector


class DouYinApp_1_9_0(App):
    def __init__(self, sip, sport, app=None):
        desired_caps = get_desired_capabilities(app, platform='7.0', device_name="SLA-TL10")
        super(DouYinApp_1_9_0, self).__init__(desired_caps, sip, sport)
        # 首页滑动翻下一个视频时等待的时间
        self.swip_to_next_wait_time = 1
        # 点击时间等待的时间
        self.click_wait_time = 2
        # 滑动翻视频、粉丝、关注列表 等待的时间
        self.swip_to_bottom_wait_time = 0.5
        # 滑动翻视频、粉丝、关注时，每做一次至底判断滑动的次数
        self.swip_times_every_assert = 10
        # 点击搜索主播/音乐人时的等待时间
        self.find_wait_time = 1
        # 编辑editor等待时间
        self.editor_wait_time = 0.5
        # 定义需要点击的元素
        self.buttons = AppButtonManager.checkout(app_version='1.9.0', device_name='SLA-TL10')
        # self.author_info_button = Button(left_top=(637, 643), right_bottom=(711, 717),  locator=(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.TextView[1]"))
        # self.author_work_button = Button(left_top=(0, 526), right_bottom=(359, 586),    locator=(By.XPATH, "//android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.TextView[contains(@text,'作品')]"))
        # self.author_like_button = Button(left_top=(360, 526), right_bottom=(720, 586),  locator=(By.XPATH, '//android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.TextView[contains(@text,"喜欢")]'))
        # self.music_info_button = Button(left_top=(636, 1117), right_bottom=(712, 1193), locator=(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.widget.TabHost/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.view.View/android.widget.FrameLayout/android.support.v4.view.ViewPager/android.widget.FrameLayout/android.view.View[1]/android.widget.FrameLayout/android.support.v4.view.ViewPager/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.ImageView[1]"))
        # self.music_hot_button = Button(left_top=(0, 498), right_bottom=(359, 566),      locator=(By.XPATH, "//android.widget.LinearLayout/android.widget.TextView[contains(@text,'热门')]"))
        # self.music_latest_button = Button(left_top=(361, 498), right_bottom=(720, 566), locator=(By.XPATH, "//android.widget.LinearLayout/android.widget.TextView[contains(@text,'最新')]"))
        # self.back_button = Button(left_top=(5, 38), right_bottom=(71, 104),             locator=(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout[2]/android.widget.RelativeLayout/android.widget.ImageView"))
        # self.author_follower_button = Button(locator=(By.XPATH, "//android.widget.LinearLayout/android.widget.TextView[contains(@text,'粉丝')]"))
        # self.author_following_button = Button(locator=(By.XPATH, "//android.widget.LinearLayout/android.widget.TextView[contains(@text,'关注')]"))
        # # self.find_button = Button(left_top=(0, 46), right_bottom=(83, 129), locator=(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.widget.TabHost/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.view.View/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ImageView[1]'))
        # self.find_button = Button(left_top=(628, 46), right_bottom=(711, 129), locator=(By.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.ImageView").instance(10)'))
        # self.find_editor_button = Button(left_top=(61, 115), right_bottom=(659, 143), locator=(By.XPATH, '//android.widget.EditText[contains(@text, "输入搜索内容")]'))
        # self.do_find_button = Button(left_top=(649, 53), right_bottom=(697, 86)
        #                             # , locator=(By.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.TextView").instance(0)'))
        #                              , locator=(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.TextView"))
        # self.first_find_result_button = Button(locator=(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[1]"))
        # self.not_update_button = Button(left_top=(314, 865), right_bottom=(406, 897), locator=(By.XPATH, "//android.widget.TextView[contains(@text,'以后再说')]"))

    def init_app(self):
        self.sleep(5)
        # self.click()
        # self.sleep(1)
        # self.click_author_info_xy()
        #
        # self.sleep(3)
        # self.click_author_like()
        # self.click_author_works()
        #
        # self.click_back()
        # self.sleep(13)
        self.close_update_widget()
        self.move_to_next()

    def capture_author_info_by_shortid(self, shortid, attrs=None):
        """
        抓取主播信息
        :param shortid: 抖音号
        :param attrs: 要抓取的信息
        """
        self.click_find_xy()
        self.input_find_keyword(shortid)
        self.click_do_find()
        self.click_first_find_result()
        if not attrs:
            attrs = ("following", "follower", "work", "like")
        if "following" in attrs:
            self.click_author_following()
            self.swip_to_bottom(2, 2, 1)
            self.click_back()
        if "follower" in attrs:
            self.click_author_follower()
            self.swip_to_bottom(2, 2, 1)
            self.click_back()
        if "work" in attrs:
            self.click_author_works()
            self.swip_to_bottom(2, 2, 1)
        if "like" in attrs:
            self.click_author_like()
            self.swip_to_bottom(2, 2, 1)
            self.click_back()

    def capture_author_info_page(self, attrs=None):
        if not attrs:
            attrs = ("following", "follower", "work", "like")

        self.click_author_info_xy()
        if "following" in attrs:
            self.click_author_following()
            self.swip_to_bottom(30, 5)
            self.click_back()
        if "follower" in attrs:
            self.click_author_follower()
            self.swip_to_bottom(50, 5)
            self.click_back()
        if "work" in attrs:
            self.click_author_works()
            self.swip_to_bottom(30, 5)
        if "like" in attrs:
            self.click_author_like()
            self.swip_to_bottom(30, 5)

        self.click_back()

    def capture_music_info_page(self):
        self.click_music_info_xy()
        self.click_music_hot()
        self.swip_to_bottom(2, 5, 1)
        self.click_music_latest()
        self.swip_to_bottom(2, 5, 1)
        self.click_back()

    def move_to_next(self):
        """
        首页翻下一个视频
        """
        self.swip(x1=int(0.5*self.window["width"]), y1=int(self.window['height']*0.9)
                  , x2=int(0.5*self.window["width"]), y2=int(self.window['height']*0.1))
        self.sleep(self.swip_to_next_wait_time)

    def swip_to_bottom(self, max_assert=None, times_once_assert=None, wait=None):
        """
            滑动至底, 滑动次数 = max_assert * times_once_assert
        :param max_assert: 最大断言（是否至底）次数
        :param times_once_assert: 每次断言（是否至底）的滑动次数
        :param wait: 每次滑动等待的时间
        """
        times_assert = 0
        while True:
            source_before = self.page_source
            for time in range(self.swip_times_every_assert if not times_once_assert else times_once_assert):
                self.swip(x1=int(0.5*self.window["width"]), y1=int(self.window['height']*0.9)
                          , x2=int(0.5*self.window["width"]), y2=int(self.window['height']*0.1))
                self.sleep(self.swip_to_bottom_wait_time if not wait else wait)
            source_after = self.page_source
            if source_before == source_after:
                break
            times_assert += 1
            if max_assert and max_assert < times_assert:
                break

    def set_up(self):
        super(DouYinApp_1_9_0, self).set_up()
        self.sleep(3)
        # self.capture_author_info_by_shortid("")
        # self.init_app()
        self.sleep(3)
        while True:
            self.move_to_next()
            self.capture_author_info_page()
            self.capture_music_info_page()

    def click_author_follower(self):
        e = self.wait_element_clickable(self.buttons['author_follower_button'].locator)
        e.click()
        self.sleep(self.click_wait_time)

    def click_author_following(self):
        e = self.wait_element_clickable(self.buttons['author_following_button'].locator)
        e.click()
        self.sleep(self.click_wait_time)

    def click_author_like_count(self):
        e = self.wait_element_clickable(self.buttons['author_like_count_button'].locator)
        e.click()
        self.sleep(self.click_wait_time)

    def click_author_info(self):
        e = self.wait_element_clickable(self.buttons['author_info_button'].locator)
        e.click()
        self.sleep(self.click_wait_time)

    def click_author_works(self):
        e = self.wait_element_clickable(self.buttons['author_work_button'].locator)
        e.click()
        self.sleep(self.click_wait_time)

    def click_author_like(self):
        e = self.wait_element_clickable(self.buttons['author_like_button'].locator)
        e.click()
        self.sleep(self.click_wait_time)

    def click_music_info(self):
        e = self.wait_element_clickable(self.buttons['music_info_button'].locator)
        e.click()
        self.sleep(self.click_wait_time)

    def click_music_hot(self):
        e = self.wait_element_clickable(self.buttons['music_hot_button'].locator)
        e.click()
        self.sleep(self.click_wait_time)

    def click_music_latest(self):
        e = self.wait_element_clickable(self.buttons['music_latest_button'].locator)
        e.click()
        self.sleep(self.click_wait_time)

    def click_author_info_xy(self):
        self.click_by_xy(self.buttons['author_info_button'].left_top, self.buttons['author_info_button'].right_bottom)
        self.sleep(self.click_wait_time)

    def click_author_works_xy(self):
        self.click_by_xy(self.buttons['author_work_button'].left_top, self.buttons['author_work_button'].right_bottom)
        self.sleep(self.click_wait_time)

    def click_author_like_xy(self):
        self.click_by_xy(self.buttons['author_like_button'].left_top, self.buttons['author_like_button'].right_bottom)
        self.sleep(self.click_wait_time)

    def click_music_info_xy(self):
        self.click_by_xy(self.buttons['music_info_button'].left_top, self.buttons['music_info_button'].right_bottom)
        self.sleep(self.click_wait_time)

    def click_music_hot_xy(self):
        self.click_by_xy(self.buttons['music_hot_button'].left_top, self.buttons['music_hot_button'].right_bottom)
        self.sleep(self.click_wait_time)

    def click_music_latest_xy(self):
        self.click_by_xy(self.buttons['music_latest_button'].left_top, self.buttons['music_latest_button'].right_bottom)
        self.sleep(self.click_wait_time)

    def click_find(self):
        self.wait_element_clickable(self.buttons['find_button'].locator).click()
        self.sleep(self.click_wait_time)

    def click_find_xy(self):
        self.click_by_xy(self.buttons['find_button'].left_top, self.buttons['find_button'].right_bottom)
        self.sleep(self.click_wait_time)

    def click_do_find(self):
        # 2018-6-27 app 界面更改，  废弃
        self.wait_element_clickable(self.buttons['do_find_button'].locator).click()
        # self.driver.press_keycode(84)

        self.sleep(self.find_wait_time)

    def click_first_find_result(self):
        self.wait_element_clickable(self.buttons['first_find_result_button'].locator).click()
        self.sleep(self.click_wait_time)

    def input_find_keyword(self, k):
        self.wait_element_clickable(self.buttons['find_editor_button'].locator).send_keys(k)
        self.sleep(self.editor_wait_time)

    def click_back(self):
        # e = self.wait_element_clickable(self.back_button.locator)
        # e.click()
        self.driver.back()
        self.sleep(self.click_wait_time)

    def click(self):
        """
        有时app会跳出一些置顶的窗口，点击屏幕时关闭。同时点击事件被消费掉
        :return:
        """
        self.click_by_xy((0, 0), tuple(self.window.values()))

    def close_update_widget(self):
        self.sleep(12)
        self.click_by_xy(self.buttons['not_update_button'].left_top, self.buttons['not_update_button'].right_bottom)

    def sleep(self, senconds):
        time.sleep(senconds)

    def do_finding(self, command, times=None):
        """
        处理搜索任务，默认重试3次
        :param command:
        :param times 又retry装饰器传过来的，第几次执行
        :return:
        """
        try:
            self.capture_author_info_by_shortid(command['data']['short_id'], attrs=command['data']['attrs'])
        except (TimeoutException, NoSuchElementException, WebDriverException) as e:
            if times == 3:
                raise DouYinFindTaskFailed(msg="抖音搜索任务失败 ")
            raise e

    def do_crawling(self, command):
        """
        处理爬虫任务，这是一个长期执行的任务,
        :param command:
        :param
        :return:
        """
        self.sleep(10)
        try:
            while True:
                self.capture_author_info_page(attrs=command['data']['attrs'])
                # self.capture_music_info_page()
                self.move_to_next()
        except (TimeoutException, NoSuchElementException, WebDriverException) as e:
            raise e

    def do(self, command, times):
        try:
            if command["task_type"] == Task.FINDING:
                self.do_finding(command, times)
            elif command["task_type"] == Task.CRAWLING:
                self.do_crawling(command)
        except DouYinFindTaskFailed as e:
            raise e


if __name__ == '__main__':
    DouYinApp_1_7_6("192.168.1.140", 4723)

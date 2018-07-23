# -*- coding: utf-8 -*-
from appium.webdriver.common.mobileby import MobileBy as By


class Button(object):
    def __init__(self, left_top=None, right_bottom=None, id=None, name=None, text=None, locator=None):
        self.left_top = left_top
        self.right_bottom = right_bottom
        self.id = id
        self.name = name
        self.text = text
        self.locator = locator
        # self.uiselector = uiselector


class AppButtonManager(object):
    @classmethod
    def checkout(cls, app_version='1.7.6', device_name=None):
        if app_version == '1.7.6':
            if device_name == 'nox':
                return cls.model_nox_simulator()
        elif app_version == '1.9.0':
            if device_name == 'SLA-TL10':
                return cls.model_huawei_720_1280()
            elif device_name == '':
                pass
        elif app_version == '2.0.0':
            if device_name == 'SLA-TL10':
                return cls.model_huawei_720_1280()
            elif device_name == 'nox':
                return cls.model_2_0_0_nox()
        elif app_version == '2.1.0':
            if device_name == 'SLA-TL10':
                return cls.model_huawei_2_1_0()
            elif device_name == 'nox':
                pass

    @classmethod
    def model_nox_simulator(cls):
        return {
            'author_info_button': Button(left_top=(637, 643), right_bottom=(711, 717), locator=(By.XPATH, "//hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.widget.TabHost/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.support.v4.view.ViewPager/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.support.v4.view.ViewPager/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.ImageView")),
            'author_work_button': Button(left_top=(0, 526), right_bottom=(359, 586), locator=(By.XPATH, "//android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.TextView[contains(@text,'作品')]")),
            'author_like_button': Button(left_top=(360, 526), right_bottom=(720, 586), locator=(By.XPATH, '//android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.TextView[contains(@text,"喜欢")]')),
            'music_info_button': Button(left_top=(636, 1117), right_bottom=(712, 1193), locator=(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.widget.TabHost/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.view.View/android.widget.FrameLayout/android.support.v4.view.ViewPager/android.widget.FrameLayout/android.view.View[1]/android.widget.FrameLayout/android.support.v4.view.ViewPager/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.ImageView[1]")),
            'music_hot_button': Button(left_top=(0, 498), right_bottom=(359, 566), locator=(By.XPATH, "//android.widget.LinearLayout/android.widget.TextView[contains(@text,'热门')]")),
            'music_latest_button': Button(left_top=(361, 498), right_bottom=(720, 566), locator=(By.XPATH, "//android.widget.LinearLayout/android.widget.TextView[contains(@text,'最新')]")),
            'back_button': Button(left_top=(5, 38), right_bottom=(71, 104), locator=(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout[2]/android.widget.RelativeLayout/android.widget.ImageView")),
            'author_follower_button': Button(locator=(By.XPATH, "//android.widget.LinearLayout/android.widget.TextView[contains(@text,'粉丝')]")),
            'author_following_button': Button(locator=(By.XPATH, "//android.widget.LinearLayout/android.widget.TextView[contains(@text,'关注')]")),
            # self.find_button = Button(left_top=(0, 46), right_bottom=(83, 129), locator=(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.widget.TabHost/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.view.View/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ImageView[1]'))
            'find_button': Button(left_top=(628, 46), right_bottom=(711, 129), locator=(By.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.ImageView").instance(10)')),
            'find_editor_button': Button(left_top=(61, 115), right_bottom=(659, 143), locator=(By.XPATH, '//android.widget.EditText[contains(@text, "输入搜索内容")]')),
            'do_find_button': Button(left_top=(649, 53), right_bottom=(697, 86), locator=(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.TextView")),
            'first_find_result_button': Button(locator=(By.XPATH, "//hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[1]")),
            'not_update_button': Button(left_top=(314, 865), right_bottom=(406, 897), locator=(By.XPATH, "//android.widget.TextView[contains(@text,'以后再说')]")),
        }

    @classmethod
    def model_2_0_0_nox(cls):
        return {
            'author_info_button': Button(left_top=(637, 643), right_bottom=(711, 717),
                                         locator=(By.XPATH, "//hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.widget.TabHost/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.support.v4.view.ViewPager/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.support.v4.view.ViewPager/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.ImageView")),
            'author_work_button': Button(left_top=(0, 526), right_bottom=(359, 586),
                                         locator=(By.XPATH, "//android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.TextView[contains(@text,'作品')]")),
            'author_like_button': Button(left_top=(360, 526), right_bottom=(720, 586),
                                         locator=(By.XPATH, '//android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.TextView[contains(@text,"喜欢")]')),
            'music_info_button': Button(left_top=(636, 1117), right_bottom=(712, 1193),
                                        locator=(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.widget.TabHost/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.view.View/android.widget.FrameLayout/android.support.v4.view.ViewPager/android.widget.FrameLayout/android.view.View[1]/android.widget.FrameLayout/android.support.v4.view.ViewPager/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.ImageView[1]")),
            'music_hot_button': Button(left_top=(0, 498), right_bottom=(359, 566),
                                       locator=(By.XPATH, "//android.widget.LinearLayout/android.widget.TextView[contains(@text,'热门')]")),
            'music_latest_button': Button(left_top=(361, 498), right_bottom=(720, 566),
                                          locator=(By.XPATH, "//android.widget.LinearLayout/android.widget.TextView[contains(@text,'最新')]")),
            'back_button': Button(left_top=(5, 38), right_bottom=(71, 104),
                                  locator=(By.XPATH, "//hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout[2]/android.widget.RelativeLayout/android.widget.ImageView")),
            'author_follower_button': Button(locator=(By.XPATH, "//android.widget.LinearLayout/android.widget.TextView[contains(@text,'粉丝')]")),
            'author_following_button': Button(locator=(By.XPATH, "//android.widget.LinearLayout/android.widget.TextView[contains(@text,'关注')]")),
            'find_button': Button(left_top=(0, 46), right_bottom=(83, 129),
                                  locator=(By.XPATH, '//hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.widget.TabHost/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.view.View/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ImageView[1]')),
            'find_editor_button': Button(left_top=(61, 49), right_bottom=(595, 77),
                                         locator=(By.XPATH, '//hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.EditText')),
            'first_find_result_button': Button(left_top=(0, 223), right_bottom=(720, 355),
                                               locator=(By.XPATH, "//hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v4.view.ViewPager/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.support.v7.widget.RecyclerView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout")),
            'not_update_button': Button(left_top=(314, 865), right_bottom=(406, 897),
                                        locator=(By.XPATH, "//android.widget.TextView[contains(@text,'以后再说')]")),
        }


    @classmethod
    def model_huawei_720_1280(cls):
        return {
            'author_info_button': Button(left_top=(610, 366), right_bottom=(708, 464), locator=(By.XPATH, "//hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.widget.TabHost/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.support.v4.view.ViewPager/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.support.v4.view.ViewPager/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.ImageView")),
            'author_work_button': Button(left_top=(129, 751), right_bottom=(230, 792), locator=(By.XPATH,
                                                                                                 "//android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.TextView[contains(@text,'作品')]")),
            'author_like_button': Button(left_top=(489, 751), right_bottom=(590, 792), locator=(By.XPATH,
                                                                                                 '//android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.TextView[contains(@text,"喜欢")]')),
            'music_info_button': Button(left_top=(591, 974), right_bottom=(720, 1110), locator=(By.XPATH,
                                                                                                 "//hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.widget.TabHost/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.support.v4.view.ViewPager/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.support.v4.view.ViewPager/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.ImageView[1]")),
            'music_hot_button': Button(left_top=(0, 498), right_bottom=(359, 566), locator=(
            By.XPATH, "//android.widget.LinearLayout/android.widget.TextView[contains(@text,'热门')]")),
            'music_latest_button': Button(left_top=(361, 498), right_bottom=(720, 566), locator=(
            By.XPATH, "//android.widget.LinearLayout/android.widget.TextView[contains(@text,'最新')]")),
            'back_button': Button(left_top=(5, 38), right_bottom=(71, 104), locator=(By.XPATH,
                                                                                     "//hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout[2]/android.widget.RelativeLayout/android.widget.ImageView")),
            'author_follower_button': Button(left_top=(468, 632), right_bottom=(528, 667),
                locator=(By.XPATH, "//android.widget.LinearLayout/android.widget.TextView[contains(@text,'粉丝')]")),
            'author_following_button': Button(left_top=(275, 632), right_bottom=(335, 667),
                locator=(By.XPATH, "//android.widget.LinearLayout/android.widget.TextView[contains(@text,'关注')]")),
            'find_button': Button(left_top=(0, 59), right_bottom=(110, 169),
                                  locator=(By.XPATH, '//hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.widget.TabHost/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.view.View/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ImageView[1]')),
            'find_editor_button': Button(left_top=(81, 63), right_bottom=(554, 99),
                                         locator=(By.XPATH, '//hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.EditText')),
            'first_find_result_button': Button(left_top=(0, 292), right_bottom=(720, 468),
                                               locator=(By.XPATH, "//hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v4.view.ViewPager/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.support.v7.widget.RecyclerView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout")),
            'not_update_button': Button(locator=(By.XPATH, "//android.widget.TextView[contains(@text,'以后再说')]")),
            'comment_button': Button(left_top=(598, 649), right_bottom=(720, 763), locator=(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.widget.TabHost/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.support.v4.view.ViewPager/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.support.v4.view.ViewPager/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]")),
            'keyboard_search': Button(left_top=(620, 1108), right_bottom=(720, 1208)),
        }

    @classmethod
    def model_huawei_2_1_0(cls):
        return {
            'author_info_button': Button(left_top=(610, 366), right_bottom=(708, 464),
                                         locator=(By.XPATH, "//hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.widget.TabHost/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.support.v4.view.ViewPager/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.support.v4.view.ViewPager/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.ImageView")),
            'author_work_button': Button(left_top=(129, 751), right_bottom=(230, 792),
                                         locator=(By.XPATH, "//android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.TextView[contains(@text,'作品')]")),
            'author_like_button': Button(left_top=(489, 751), right_bottom=(590, 792),
                                         locator=(By.XPATH, '//android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.TextView[contains(@text,"喜欢")]')),
            'music_info_button': Button(left_top=(591, 974), right_bottom=(720, 1110),
                                        locator=(By.XPATH, "//hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.widget.TabHost/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.support.v4.view.ViewPager/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.support.v4.view.ViewPager/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.ImageView[1]")),
            'music_hot_button': Button(left_top=(0, 498), right_bottom=(359, 566),
                                       locator=(By.XPATH, "//android.widget.LinearLayout/android.widget.TextView[contains(@text,'热门')]")),
            'music_latest_button': Button(left_top=(361, 498), right_bottom=(720, 566),
                                          locator=(By.XPATH, "//android.widget.LinearLayout/android.widget.TextView[contains(@text,'最新')]")),
            'back_button': Button(left_top=(5, 38), right_bottom=(71, 104),
                                  locator=(By.XPATH, "//hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout[2]/android.widget.RelativeLayout/android.widget.ImageView")),
            'author_follower_button': Button(left_top=(468, 632), right_bottom=(528, 667),
                                             locator=(By.XPATH, "//android.widget.LinearLayout/android.widget.TextView[contains(@text,'粉丝')]")),
            'author_following_button': Button(left_top=(275, 632), right_bottom=(335, 667),
                                              locator=(By.XPATH,  "//android.widget.LinearLayout/android.widget.TextView[contains(@text,'关注')]")),
            'find_button': Button(left_top=(0, 59), right_bottom=(110, 169),
                                  locator=(By.XPATH, '//hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.widget.TabHost/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.view.View/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ImageView[1]')),
            'find_editor_button': Button(left_top=(81, 63), right_bottom=(554, 99),
                                         locator=(By.XPATH, '//hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.EditText')),
            'first_find_result_button': Button(left_top=(0, 292), right_bottom=(720, 468),
                                               locator=(By.XPATH, "//hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v4.view.ViewPager/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.support.v7.widget.RecyclerView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout")),
            'not_update_button': Button(locator=(By.XPATH, "//android.widget.TextView[contains(@text,'以后再说')]")),
            'comment_button': Button(left_top=(598, 649), right_bottom=(720, 763), locator=(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.widget.TabHost/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.support.v4.view.ViewPager/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.support.v4.view.ViewPager/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]")),
            'keyboard_search': Button(left_top=(620, 1108), right_bottom=(720, 1208)),
        }
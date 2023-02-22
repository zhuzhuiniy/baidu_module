import unittest
from selenium import webdriver

from page.douyin.douyin_home import DyPage
from page.help_page import HelpPage
from page.home_page import HomePage


class TestHelp(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.baidu.com")

        # 创建页面对象
        self.dy_home_page = DyPage(self.driver)
        self.home_page = HomePage(self.driver)
        self.help_page = HelpPage(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_dy_home_center(self):
        # 百度搜索抖音
        self.dy_home_page.get_first_dy_text()
        # 点击搜索按钮
        self.dy_home_page.get_first_baidu_search_text()
        # 点击第一个抖音首页
        self.dy_home_page.get_first_dy_home_text()
        # 切换窗口
        self.driver.switch_to.window(self.driver.window_handles[-1])
        # 点击登陆页面
        self.dy_home_page.get_first_dy_login_text()
        # 输入手机号
        self.dy_home_page.get_first_dy_mobile()
        self.dy_home_page.get_first_dy_password()
        self.dy_home_page.get_first_dy_login_button()
        # 输入密码
        # 点击登陆
        # 帮助页面 - 获取第一个热词
        # word = self.help_page.get_first_hotword_text()
        word = self.driver.current_url

        # 断言： 第一个热词是不是叫做"百度账号被封禁"
        assert "douyin" in word

    # def test_help_center1(self):
    #     # 首页 - 点击 帮助中心
    #     self.home_page.click_help_center()
    #
    #     self.driver.switch_to.window(self.driver.window_handles[-1])
    #
    #     # 帮助页面 - 获取第一个热词
    #     word = self.help_page.get_first_hotword_text()
    #
    #     print(word)
    #
    #     # 断言： 第一个热词是不是叫做"百度账号被封禁"
    #     assert "辟谣" in word

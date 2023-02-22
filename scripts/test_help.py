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
        # 百度搜索抖音 - 点击首页
        self.dy_home_page.get_first_dy_text()
        self.dy_home_page.get_first_baidu_search_text()
        self.dy_home_page.get_first_dy_home_text()

        self.driver.switch_to.window(self.driver.window_handles[-1])

        # 帮助页面 - 获取第一个热词
        # word = self.help_page.get_first_hotword_text()
        word = self.driver.current_url
        print("111111111111", word)

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

from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class HelpPage(BaseAction):
    # ------ 元素的特征 ------
    # help_center_button = By.LINK_TEXT, "帮助中心"
    hotword_feature = By.XPATH, "//*[@class='back']/a"

    # ------ 对元素的操作 ------
    # def click_help_center(self):
    #     self.click(self.help_center_button)

    def get_first_hotword_text(self):
        return self.get_text(self.hotword_feature)

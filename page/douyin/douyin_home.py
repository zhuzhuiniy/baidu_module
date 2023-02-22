from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class DyPage(BaseAction):
    # ------ 元素的特征 ------
    # help_center_button = By.LINK_TEXT, "帮助中心"
    dy_feature = By.XPATH, '//*[@id="kw"]'
    # baidu_search = By.ID, 'su'
    baidu_search = By.XPATH, '//*[@id="su"]'
    dy_home_feature = By.XPATH, '//*[@id="1"]/div/div[1]/h3/a[1]'
    # ------ 对元素的操作 ------
    # def click_help_center(self):
    #     self.click(self.help_center_button)

    def get_first_dy_text(self):
        return self.input(self.dy_feature, "抖音")

    def get_first_baidu_search_text(self):
        return self.click(self.baidu_search)

    def get_first_dy_home_text(self):
        return self.click(self.dy_home_feature)

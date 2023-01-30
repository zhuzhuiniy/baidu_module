from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class HomePage(BaseAction):
    # ------ 元素的特征 ------
    help_center_button = By.LINK_TEXT, "帮助中心"

    # 按钮：xxx_button
    # 输入框：xxx_edit_text
    # 文本框：xxx_label

    # ------ 对元素的操作 ------
    def click_help_center(self):
        self.click(self.help_center_button)

    # 点击：click_xxx
    # 输入：input_xxx
    # 清空：clear_xxx
    # 获取文字：get_xxx_text
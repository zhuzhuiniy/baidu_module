from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class DyPage(BaseAction):
    # ------ 元素的特征 ------
    # 百度搜索输入框
    dy_feature = By.XPATH, '//*[@id="kw"]'
    # 百度搜索按钮
    baidu_search = By.ID, 'su'
    # 点击抖音首页
    dy_home_feature = By.XPATH, '//*[@id="1"]/div/div[1]/h3/a[1]'
    # 点击账户密码登陆
    dy_login = By.XPATH, '//*[@id="web-login-container"]/article/article/article/div[1]/ul[1]/li[3]'
    # 手机号输入框
    du_login_input_mobile = By.XPATH, '//*[@id="web-login-container"]/article/article/article/form/div[1]/div/input'
    # 密码输入框
    du_login_input_password = By.XPATH, '//*[@id="web-login-container"]/article/article/article/form/div[2]/div/div/input'
    # 登陆按钮
    du_login_button = By.XPATH, '//*[@id="web-login-container"]/article/article/article/form/div[5]/button'

    def get_first_dy_text(self):
        return self.input(self.dy_feature, "抖音")

    def get_first_baidu_search_text(self):
        return self.click(self.baidu_search)

    def get_first_dy_home_text(self):
        return self.click(self.dy_home_feature)

    def get_first_dy_login_text(self):
        return self.click(self.dy_login)

    def get_first_dy_mobile(self):
        return self.input(self.du_login_input_mobile, "17610115330")

    def get_first_dy_password(self):
        return self.input(self.du_login_input_password, "Zhubaojia123")

    def get_first_dy_login_button(self):
        return self.click(self.du_login_button)

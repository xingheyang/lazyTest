# project  :McenterSystem
# -*- coding = UTF-8 -*-
# Autohr   :buxiubuzhi
# File     :RegisterService.py
# time     :2020/11/28  14:46
# Describe : 注册流程
# ---------------------------------------
import allure

from pages.RegisterPage import RegisterPage


@allure.feature("注册业务")
class RegisterService:

    def __init__(self, driver):
        self.r = RegisterPage(driver)

    @allure.story("用户注册")
    def userRegister(self, account, username, password, repassword, issue, answer):
        print("----->",self.r)
        print("----->",self)
        self.r.getRegisterPage()
        self.r.inputAccount(account)
        self.r.inputUsername(username)
        self.r.inputPassword(password)
        self.r.inputRepassword(repassword)
        self.r.inputIssue(issue)
        self.r.inputAnswer(answer)
        self.r.clickSubmit()
        return self.reg.getalertText()

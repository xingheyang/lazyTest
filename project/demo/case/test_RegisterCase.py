# project  :McenterSystem
# -*- coding = UTF-8 -*-
# Autohr   :XingHeYang
# File     :test_RegisterCase.py
# time     :2020/11/28  14:55
# Describe : 注册的测试用例
# ---------------------------------------
import allure
import pytest

import lazyTest
from service.RegisterService import RegisterService


class TestRegister(lazyTest.TestCase):

    @pytest.fixture(scope="function")
    def setUp(self, getdriver, flush_browser):
        self.reg = RegisterService(getdriver)

    @allure.title("用户注册")
    def testRegister(self, setUp):
        account = lazyTest.createData("account{}")
        result = self.reg.userRegister(account, account, "123456", "123456", "问题", "答案")
        assert result == "注册成功,快去登录吧！"

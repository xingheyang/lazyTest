
# project  :Python_project
# -*- coding = UTF-8 -*-
# Autohr   : 
# File     : conftest.py
# time     : 
# Describe :
# ---------------------------------------
import os
import sys
import time

import allure
import pytest

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from service.loginService import LoginService

globals()["driver"] = None


def pytest_addoption(parser):
    # 添加参数到pytest.ini
    parser.addini('Terminal', help='访问浏览器参数')
    parser.addini('URL', help='添加 url 访问地址参数')
    parser.addini('filepath', help='添加 截图路径')
    parser.addini('logpath', help='添加 日志路径')
    parser.addini('username', help='用户名')
    parser.addini('password', help='密码')


@pytest.fixture(scope='session')
def getdriver(pytestconfig):
    Terminal = pytestconfig.getini("Terminal")
    URL = pytestconfig.getini("URL")
    driver = browser_Config(Terminal, URL)
    globals()["driver"] = driver.base_driver
    login = LoginService(driver)
    login.login(pytestconfig.getini("username"), pytestconfig.getini("password"))
    yield driver
    driver.browser_close()


@pytest.fixture(scope="function")
def flush_browser(getdriver):
    yield
    getdriver.flush_browser()
    getdriver.sleep(1)


# 用例出现异常或失败时截图
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    config = item.config
    outcome = yield
    report = outcome.get_result()
    if report.when == 'call':
        xfail = hasattr(report, 'wasxfail')
        if report.failed and not xfail:
            project = str(config.rootpath)
            filepath = config.getini("filepath")
            picture_time = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime(time.time()))
            filename = project + filepath + picture_time + ".png"
            globals()["driver"].save_screenshot(filename)
            with open(filename, "rb") as f:
                file = f.read()
                allure.attach(file, "失败截图", allure.attachment_type.PNG)


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_setup(item):
    config = item.config
    project = str(config.rootpath)
    logpath = config.getini("logpath")
    logging_plugin = config.pluginmanager.get_plugin("logging-plugin")
    logging_plugin.set_log_path(project + logpath)
    yield

    
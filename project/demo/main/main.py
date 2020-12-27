
import os
import sys
import time

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from lazyTest import ClearTestResult


def getPorjectPath():
    '''
    获取项目路径
    '''
    return os.path.dirname(os.path.dirname(__file__))


def clearLogAndReport():
    print("----------清空上次测试结果----------")
    path = getPorjectPath() + "/result"
    ClearTestResult(path)
    time.sleep(2)
    print("----------测试结果清空成功----------")


def runlastFailed():
    print("启动失败用例重跑")
    cmd = "pytest -s --lf {}/case --alluredir {}/result/report".format(getPorjectPath(), getPorjectPath())
    print(os.system(cmd))


def startReport():
    print("-------------启动测试报告--------------")
    cmd = "allure serve {}/result/report".format(getPorjectPath())
    print(os.system(cmd))


def startCase(cases):
    print("------------开始执行测试------------")
    cmd = "pytest -s {}/case/{} --alluredir {}/result/report".format(getPorjectPath(), cases, getPorjectPath())
    print(os.system(cmd))


def run(cases=" "):
    clearLogAndReport()
    startCase(cases)
    s = input("请选择要启用的服务:1:启动失败用例重跑;	2：启动测试报告;")
    if s == "1":
        runlastFailed()
        s = input("是否启动测试报告:y/n")
    if s == "2" or s == "y":
        startReport()


run()
    
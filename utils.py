# -*- coding = UTF-8 -*-
# Autohr   : buxiubuzhi
# File     : utils.py
# project  : Python_project
# time     : 2020/11/16 17:01
# Describe : 工具类
# ---------------------------------------

import datetime
import os
import time
import functools


from lazyTest.file import YamlOperation, IniFileOperation, FileOperation, JsonFileOperation


def Sleep(s: int = 1):
    """
    每个用例的强制休眠。
    """

    def Sleep(func):
        nonlocal s

        @functools.wraps(func)
        def inner(*args):
            time.sleep(s)
            result = func(*args)
            time.sleep(s)
            return result

        return inner

    return Sleep


def createData(body: str = "auto{}"):
    """
    返回给定字符串拼接上时间后的字符
    """
    nowTime = datetime.datetime.strftime(datetime.datetime.now(), "%Y%m%d%H%M")[2:]
    return body.format(nowTime)


def getPorjectPath():
    """
    获取项目路径
    """
    return os.path.dirname(os.path.dirname(__file__))


def ClearTestResult(path: str):
    """
    清空目录中的文件
    参数：path：将会清除该目录下的所有文件，包括子目录文件；
    """
    for i in os.listdir(path):
        path_file = os.path.join(path, i)
        if os.path.isfile(path_file):
            os.remove(path_file)
        else:
            ClearTestResult(path_file)


def readElementSource(fileName: str) -> FileOperation:
    """
    根据文件后缀名创建对应的读取对象
    """
    if fileName != "" and fileName is not None:
        if fileName.endswith(".yaml"):
            return YamlOperation(fileName)
        elif fileName.endswith(".json"):
            return JsonFileOperation(fileName)
        elif fileName.endswith(".ini"):
            return IniFileOperation(fileName)
        else:
            raise Exception("文件类型错误")

def writeElementKey(filepath,fileName,fileType,data : dict):
    # 得到完整文件路径
    realFile =  filepath + fileName + '.' + fileType
    if os.path.exists(realFile):
        print("文件已存在不进行写入")
    else:
        newdata = {}
        for i in data:
            newdata[i.upper()] = None
            for j in data[i]:
                newdata[j.upper()] = None
        YamlOperation.writeFileToDict(realFile,newdata)
        print("文件写入成功！！！")


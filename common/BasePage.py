# -*- coding:utf-8 -*-
# from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from appium.webdriver.common.mobileby import By
from config.config import *
from utils.parseYaml import parseYaml


"""
create_time:2018/11/12 12:37
file:BasePage.py
@author:宁同刚
"""


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver
        self.eleInfo = parseYaml(eleInfoPath)

    def getEleInfo(self):
        return self.eleInfo

    # 获取单个页面元素对象
    def getElement(self, locateType, locatorExpression):
        try:
            element = WebDriverWait(self.driver, WAIT_TIME).until(
                lambda x: x.find_element(by=locateType, value=locatorExpression))
            return element
        except Exception as e:
            raise e

    # 获取多个页面元素对象，以list返回
    def getElements(self, locateTye, locatorExpression):
        try:
            elements = WebDriverWait(self.driver, 30).until(lambda x: x.find_elements(by=locateTye, value=locatorExpression))
            return elements
        except Exception as e:
            raise e


if __name__ == '__main__':
    pass


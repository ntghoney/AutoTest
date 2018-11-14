# -*- coding:utf-8 -*-
"""
create_time:2018/11/12 16:17
file:BaIduPage.py
@author:宁同刚
"""
from common.BasePage import BasePage
from selenium import webdriver
from utils.log import logs

class Baidu(BasePage):
    logs=logs()
    def __getBaiduEle(self):
        info=self.eleInfo.getValue("baidu")
        logs.info(info)
        return info

    def inputKeyWords(self,keywords):
        self.logs.info("查找关键字输入框")
        lt,le=self.__getBaiduEle()["search_input"].split(">")
        self.logs.info("输入{}".format(keywords))
        self.getElement(lt,le).send_keys(keywords)
    def clickSearch(self):
        self.logs.info("查找搜索按钮")
        lt,le=self.__getBaiduEle()["ok_btn"].split(">")
        self.logs.info("点击搜搜按钮")
        self.getElement(lt, le).click()

if __name__ == '__main__':
    logs=logs()
    driver=webdriver.Chrome()
    logs.info("正在 打开百度")
    driver.get("http://www.baidu.com")
    bd=Baidu(driver)
    bd.inputKeyWords(u"你好")
    bd.clickSearch()
    logs.info("执行完毕，关闭浏览器")
    driver.quit()



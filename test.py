# -*- coding:utf-8 -*-
from selenium import webdriver
from common.BasePage import BasePage

"""
create_time:2018/11/12 13:34
file:test.py
@author:宁同刚
"""
from utils.parseExcel import ParseExcel
pe=ParseExcel(r"C:\ntg\SimpletAutoTest\data\case.xlsx")
s=pe.readRowValue(1,0)
print(s)
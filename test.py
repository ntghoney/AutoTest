# -*- coding:utf-8 -*-
from selenium import webdriver
from common.BasePage import BasePage

"""
create_time:2018/11/12 13:34
file:test.py
@author:宁同刚
"""
from utils.parseExcel import ParseExcel
it1=[1,2,3,4,5]
it2=[5,4,3,2,1]
for i1,i2 in it1,it2:
    print(i1,i2)
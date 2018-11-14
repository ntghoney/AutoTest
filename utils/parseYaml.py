# -*- coding:utf-8 -*-
"""
create_time:2018/11/12 13:42
file:parseYaml.py
@author:宁同刚
"""
import yaml


# -*- coding:utf-8 -*-

class parseYaml:
    def __init__(self, homeyaml):
        self.filePath = homeyaml

    def __getYam(self):
        try:
            with open(self.filePath, encoding='utf-8') as f:
                return yaml.load(f)
        except FileNotFoundError:
            print(u"找不到文件")

    def getValue(self, key):
        return self.__getYam().get(key)




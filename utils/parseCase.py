# -*- coding:utf-8 -*-
"""
create_time:2018/11/13 17:59
file:parseCase.py
@author:宁同刚
"""
from utils.parseExcel import ParseExcel
from config.config import *


class ParseCase:
    def __init__(self, casePath, msheet):
        self.pe = ParseExcel(casePath)
        self.sheet = msheet

    def getCases(self):
        cases=[]
        keys=["caseId","caseTitle","casePage","caseStep","caseExcept","caseResult","caseIsSuccess"]
        for row in range(1,self.pe.getNrows(self.sheet)):
            case=self.pe.getRowValue(self.sheet,row)
            cases.append(dict(zip(keys,case)))
        return cases



if __name__ == '__main__':
    pc = ParseCase(casePath, 1)
    cases=pc.getCases()
    for case in cases:
        for item in case.keys():
            if item == "caseStep":
                steps = case[item].split("\n")
                print(steps)


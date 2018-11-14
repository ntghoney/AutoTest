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
        caseList = []  # 用例集
        stepDic = {}  # 步骤
        exceptDic = {}  # 预期结果
        keys = ["caseId", "caseTitle", "casePage", "caseStep", "caseData", "caseExcept", "caseResult", "caseIsSuccess"]
        for row in range(1, self.pe.getNrows(self.sheet)):
            case = self.pe.getRowValue(self.sheet, row)
            _steps = self.pe.getCellValue(self.sheet, row, 3)
            _datas = self.pe.getCellValue(self.sheet, row, 4)
            _excepts = self.pe.getCellValue(self.sheet, row, 5)
            # steps = ""
            # datas = ""
            excepts = ""
            # steps = self.pe.getCellValue(self.sheet, row, 3).split("\n")
            # datas=self.pe.getCellValue(self.sheet, row, 4).split("\n")
            # excepts = self.pe.getCellValue(self.sheet, row, 5).split("\n")
            # if _steps!="":
            #     steps = self.pe.getCellValue(self.sheet, row, 3).split("\n")
            # if _datas!="":
            #     datas = self.pe.getCellValue(self.sheet, row, 4).split("\n")
            # if _excepts!="":
            #     excepts = self.pe.getCellValue(self.sheet, row, 5).split("\n")
            # 获得操作步骤转换为字典
            if _steps != "":
                steps = self.pe.getCellValue(self.sheet, row, 3).split("\n")
                for itemStep in steps:
                    stepNo, stepOpea = itemStep.split("、")
                    stepDic[stepNo] = stepOpea
                    case[3] = stepDic
            # 获得测试数据转换为字典
            for itemExpect in excepts:
                exceptNo, exceptOpea = itemExpect.split("、")
                exceptDic[exceptNo] = exceptOpea
                case[5] = exceptDic

            # 获得预期结果转换为字典
            if _excepts != "":
                excepts = self.pe.getCellValue(self.sheet, row, 5).split("\n")
                for itemExpect in excepts:
                    exceptNo, exceptOpea = itemExpect.split("、")
                    exceptDic[exceptNo] = exceptOpea
                    case[5] = exceptDic
            caseList.append(dict(zip(keys, case)))

        return caseList


if __name__ == '__main__':
    pc = ParseCase(casePath, 1)
    cases = pc.getCases()
    # for case in cases:
    #     for item in case.keys():
    #         if item == "caseStep":
    #             steps = case[item].split("\n")
    #             print(steps)
    print(cases)

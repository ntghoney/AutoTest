# -*- coding:utf-8 -*-
"""
create_time:2018/11/13 16:42
file:parseExcel.py
@author:宁同刚
"""
import xlrd, xlwt
from xlutils import copy
import os
from config.config import *


class ParseExcel:
    def __init__(self, filePath):
        self.filePath = filePath
        if os.path.isfile(filePath):
            self.wb = xlrd.open_workbook(filePath)
        else:
            raise Exception(u"{}文件不存在".format(filePath))

    def __getSheet(self, msheet):
        sheet = ""
        if isinstance(msheet, int):
            sheet = self.wb.sheet_by_index(msheet)
        if isinstance(msheet, str):
            sheet = self.wb.sheet_by_name(msheet)
        return sheet

    def getNrows(self, msheet):
        return self.__getSheet(msheet).nrows

    def getNcols(self, msheet):
        return self.__getSheet(msheet).ncols

    # 获得表中整行的数据
    def getRowValue(self, msheet, row):
        # assert isinstance(sheet, xlrd.sheet.Sheet)
        rowValue = []
        sheet = self.__getSheet(msheet)
        ncols = self.getNcols(msheet)
        for col in range(ncols):
            cell = sheet.cell_value(row, col)
            rowValue.append(cell)
        return rowValue

    # 按行获得表中所有的数据
    def getAllData(self, sheet):
        data = []
        for row in range(1, self.getNrows(sheet)):
            data.append(self.getRowValue(sheet, row))
        return data

    #获得整例的数据
    def getColValue(self, msheet, col):
        colValue = []
        sheet = self.__getSheet(msheet)
        nrows = self.getNrows(msheet)
        for row in range(nrows):
            cell = sheet.cell_value(row, col)
            colValue.append(cell)
        return colValue

    #获得单元格的数据
    def getCellValue(self,msheet,row,col):
        sheet=self.__getSheet(msheet)
        return sheet.cell_value(row,col)




if __name__ == '__main__':
    pe = ParseExcel(casePath)
    s = pe.getColValue(1, 3)
    print(s)

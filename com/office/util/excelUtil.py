#!/usr/bin/python
#-*-coding:UTF-8-*-
# encoding=utf8
from com.office.util.fileUtil import getFiles
def read(filename, sheetName='Sheet1'):
    import xlrd
    data = xlrd.open_workbook(filename);
    table = data.sheet_by_name(sheetName)
    nrows = table.nrows
    returnList = [];
    for i in range(nrows ):
        returnList.append(table.row_values(i))
    return returnList;

def write(tableData, filename, sheetName='Sheet1'):
    import xlwt
    wb=xlwt.Workbook()
    ws=wb.add_sheet(sheetName)
    for i in range(len(tableData)):
        rowDatas = tableData[i];
        for j in range(len(rowDatas)):
            ws.write(i,j,rowDatas[j])
    wb.save(filename)
    
def writeExcel(tableData, filename, sheetName='Sheet1'):
    from openpyxl import Workbook
    wb = Workbook()
    ws = wb.create_sheet(sheetName, 0)
    
    for i in range(len(tableData)):
        rowDatas = tableData[i];
        if type(rowDatas) != list:
            rowDatas = [rowDatas];
        ws.append(rowDatas)
    # Save the file
    wb.save(filename)
    
if __name__ == "__main__":
    totalData = [range(260)]
    writeExcel(totalData, "total.xls")

#!/usr/bin/python
# encoding=utf8
def read(filename, sheetName='Sheet1'):
    import xlrd
    data = xlrd.open_workbook(filename);
    table = data.sheet_by_name(sheetName)
    nrows = table.nrows
    returnList = [];
    for i in range(nrows ):
        returnList.append(table.row_values(i))
    return returnList;
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
    pass

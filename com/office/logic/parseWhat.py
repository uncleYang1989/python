#!/usr/bin/python
#-*-coding:UTF-8-*-
# encoding=utf8


def parseWhat(pathname):
    import xlrd
    data = xlrd.open_workbook(pathname);
    table = data.sheet_by_name('Sheet1')#通过名称获取
    nrows = table.nrows
    
    #用来存放结果列表
    tableCache = []
    
    #暂存C列和D列的数据
    newIngredientCache = [];
    
    #循环表格
    for i in range(nrows ):
        
        #第一列是标题，跳过
        if i ==0:
            continue
        
        #获取列数据
        rowData = table.row_values(i);
        
        #结果表的行
        newRowData = []
        
        #A列默认添加
        newRowData.append(rowData[0])
        
        #如果有C列，就暂存起来
        if rowData[2]:
            newIngredientCache.append([rowData[2], rowData[3]])
            
        #如果B列有数据，就在C列添加TCMID
        if rowData[1]:
            newRowData.append(rowData[1])
            newRowData.append("TCMID")
        else:
        #B列没有数据，则填充之前暂存的C列数据
            if newIngredientCache:
                #取出第一列数据
                tmp = newIngredientCache[0]
                #在暂存区里删除第一列数据
                newIngredientCache = newIngredientCache[1:]
                newRowData.append(tmp[0])
                newRowData.append(tmp[1])
                
        #将新生成的行数据保存到结果列表
        tableCache.append(newRowData)
    
    #如果暂存区里还有数据，则需要添加到B列里
    for tmp in newIngredientCache:
        newRowData = []
        newRowData.append("")
        newRowData.append(tmp[0])
        newRowData.append(tmp[1])
        tableCache.append(newRowData)
        
    #使用xlwt写入新的文件中去
    import xlwt
    wb=xlwt.Workbook()
    ws=wb.add_sheet('sheet1')
    for i in range(len(tableCache)):
        rowDatas = tableCache[i];
        for j in range(len(rowDatas)):
            ws.write(i,j,rowDatas[j])
    import os
    wb.save(os.path.splitext(pathname)[0]+ "_res.xls")

if __name__ == "__main__":
    pathname = u"六神曲.xlsx";
    parseWhat(pathname);

#!/usr/bin/python
# -*-coding:UTF-8-*-
# encoding=utf8
# -*- coding: cp936 -*-
#This script is using in MIC only,Powered by rexchenhan
#养老保险公司比例
EI_CoRate=0.323
#养老保险个人比例
EI_EmpRate=0.105
#公积金公司比例
HF_CoRate=0.12
#公积金个人比例
HF_EmpRate=0.12
#个税起征点
Threshold=3500

#

Emp_Salary=int(raw_input ('请输入你的税前薪水：'))
#Start to calculate
EI_Emp=Emp_Salary*EI_EmpRate
EI_Co=Emp_Salary*EI_CoRate
HF_Emp=Emp_Salary*HF_EmpRate
HF_Co=Emp_Salary*HF_CoRate
Emp_Sal_Before_Tax=Emp_Salary-(HF_Emp+EI_Emp)
Sal_NeedTax=Emp_Sal_Before_Tax-Threshold
Tax=0.0
Final_Cash=0.0
#calculate TAX
if Sal_NeedTax<=0:
        Tax=0.0
elif Sal_NeedTax<1500:
        Tax=Sal_NeedTax*0.03
elif Sal_NeedTax<4500:
        Tax=Sal_NeedTax*0.1-105
elif Sal_NeedTax<9000:
        Tax=Sal_NeedTax*0.2-555
elif Sal_NeedTax<35000:
    Tax=Sal_NeedTax*0.25-1005
elif Sal_NeedTax<55000:
        Tax=Sal_NeedTax*0.3-2775
elif Sal_NeedTax<80000:
        Tax=Sal_NeedTax*0.35-5505
else:Tax=Sal_NeedTax*0.45-13505

Final_Cash=Emp_Sal_Before_Tax-Tax
#Start to print the result
Str1='住房公积金缴纳：个人承担：%6.1f  公司承担：%6.1f' % (HF_Emp,HF_Co)
Str2='养老保险金缴纳：个人承担：%6.1f  公司承担：%6.1f' % (EI_Emp,EI_Co)
Str3='扣除各类保险后,需缴税部分：%6.1f' % Emp_Sal_Before_Tax
Str4='您需要缴税：%6.1f' % Tax
Str5='您的最终收入：%6.1f' % Final_Cash
print '*'*60
print Str1
print Str2
print Str3
print Str4
print Str5
# -*- coding: UTF-8 -*-

import tax

month = input("请输入月份:")
income = input("请输入工资:")
tax_free_income = input("请输入免税收入:")
security_n_fund = input("请输入专项扣除(三险一金):")
special_deduction = input("请输入专项附加扣除:")
other_deduction = input("请输入依法确定的其他扣除:")


#print m, ic, tfic, snf, sd, od

print tax.calculator(month, income, tax_free_income, security_n_fund, 5000, special_deduction, other_deduction)

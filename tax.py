#!/usr/bin/python
# -*- coding: UTF-8 -*-

#获取相应的层级，税率和速算扣除数，返回一个元组
def r_n_d(taxable_income):
    #level
    lv = [0, 36000, 144000, 300000, 420000, 660000, 960000]
    #tax rate
    r = [0.03, 0.1, 0.2, 0.25, 0.3, 0.35, 0.45]
    #quick deduction
    d = [0, 2520, 16920, 31920, 52920, 85920, 181920]
    if taxable_income <= lv[1]:
        tr = r[0] #tax_rate
        qd = d[0] #quick_deduction
        return lv[0], tr, qd
    elif taxable_income > lv[1] and taxable_income <= lv[2]:
        tr = r[1]
        qd = d[1]
        return lv[1], tr, qd
    elif taxable_income > lv[2] and taxable_income <= lv[3]:
        tr = r[2]
        qd = d[2]
        return lv[2], tr, qd
    elif taxable_income > lv[3] and taxable_income <= lv[4]:
        tr = r[3]
        qd = d[3]
        return lv[3], tr, qd
    elif taxable_income > lv[4] and taxable_income <= lv[5]:
        tr = r[4]
        qd = d[4]
        return lv[4], tr, qd
    elif taxable_income > lv[5] and taxable_income <= lv[6]:
        tr = r[5]
        qd = d[5]
        return lv[5], tr, qd
    else:
        tr = r[6]
        qd = d[6]
        return lv[6], tr, qd

#个税计算器
def calculator(month, income, tax_free_income, security_n_fund, tax_threshold, special_deduction, other_deduction):
    #根据月份，确定每月的累计应税额
    taxable_income_by_month = []
    i = 0
    while i < month:
        i+=1
        current_taxable_income = (income - tax_free_income - security_n_fund - tax_threshold - special_deduction - other_deduction)*i
        taxable_income_by_month.append(round(current_taxable_income,2))
    #根据每月的累计应税所得额，找到相应的税率和速算扣除数，得到每月的应预扣预缴税额
    #这里假设了每月工资相同，所有的扣除项目也都相同
    total_tax = []
    rate_by_month = []
    deduction_by_month = []
    for item in taxable_income_by_month:
        current_rate = r_n_d(item)[1]
        rate_by_month.append(current_rate)
        current_deduction = r_n_d(item)[2]
        deduction_by_month.append(current_deduction)
        total_tax_item = item * current_rate - current_deduction
        total_tax.append(round(total_tax_item,2))
    #本期应预扣预缴税额 = 最后一个月的累计应预扣预缴税额-上个月的累计应预扣预缴税额
    if len(total_tax) > 1:
        paid_tax = total_tax[-2]
        current_tax = total_tax[-1]-paid_tax
    else:
        current_tax = total_tax[-1]
    #本期应预扣预缴税额最小为0
    if current_tax < 0:
        current_tax = 0

    #print rate_by_month
    #print deduction_by_month
    #print taxable_income_by_month
    #print total_tax
    #print paid_tax
    return current_tax

#!/usr/bin/python
# -*- coding: UTF-8 -*-

# CGI处理模块
import cgi, cgitb
import tax

# 创建 FieldStorage 的实例化
form = cgi.FieldStorage()

month = form.getvalue('month')
income = form.getvalue('income')
tax_free_income = form.getvalue('tax_free_income')
security_n_fund = form.getvalue('security_n_fund')
special_deduction = form.getvalue('special_deduction')
other_deduction = form.getvalue('other_deduction')

month = int(month)
income = round(float(income),2)
tax_free_income = round(float(tax_free_income),2)
security_n_fund = round(float(security_n_fund),2)
special_deduction = int(special_deduction)
other_deduction = int(other_deduction)

tax = tax.calculator(month, income, tax_free_income, security_n_fund, 5000, special_deduction, other_deduction)

print "Content-type:text/html"
print
print "<html>"
print "<head>"
print "<meta charset=\"utf-8\">"
print "<title>2019个税计算器</title>"
print "</head>"
print "<body>"
print "<h2>%s</h2>" % tax
#print "<h2>%s %s %s %s %s %s</h2>" % (month, income, tax_free_income, security_n_fund, special_deduction, other_deduction)
print "</body>"
print "</html>"

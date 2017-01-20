#!D:\Program Files\Python27\python
# coding=utf-8

boundary = [(0, 0), (10, 0.1), (20, 0.075), (40, 0.05), (60, 0.03), (100, 0.015), (10000000, 0.01)]
print boundary

revenue_s = raw_input("净利润(万元）：")
revenue = int(revenue_s)
print revenue

salary = 0.0

for i in range(1, len(boundary) + 1):
    print boundary[i-1]
    if revenue > boundary[i][0]:
        salary += (boundary[i][0] - boundary[i-1][0])*boundary[i][1]
    else:
        salary += (revenue - boundary[i-1][0]) * boundary[i][1]
        break

print "total salary: ", salary*10000



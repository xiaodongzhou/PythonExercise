#!D:\Program Files\Python27\python
# coding=utf-8

all_num = set();

for i in range(1, 5):
    for j in range(1, 5):
        for k in range(1, 5):
            if (i!=k and i!=j and j!=k):
                curr_num = 100*i+10*j+k ;
                all_num.add(curr_num)

print all_num;

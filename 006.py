#!D:\Program Files\Python27\python
# coding=utf-8

def fib(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a+b
        print a
    return a

#print fib(10)
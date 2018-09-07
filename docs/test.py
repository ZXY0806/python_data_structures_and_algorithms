# -*- coding:utf-8 -*-
def test1():
    try:
        print(1/0)
    except ZeroDivisionError:
        raise ValueError
def test2():
    st = '3'*2
    print(st)
def test3():
    str1 = '"--"'
    print(str1)
test3()


# -*- coding:utf-8 -*-
a = 2
b = 1
a, b = b, a
print(a, b)
a = b
b = a
print(a, b)

L = [1, 2, 3]
L[0], L[1] = L[1], L[0]
print(L[0], L[1])
L[0] = L[1]
L[1] = L[0]
print(L[0], L[1])

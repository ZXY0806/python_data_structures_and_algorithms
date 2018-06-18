# -*- coding: utf-8 -*-

# https://docs.python.org/2/library/array.html
from array import array    # python 提供的比较原始的 array 类


arr = array('u', 'asdf')

print(arr[0], arr[1], arr[2], arr[3])


# 实现定长的 Array ADT，省略了边界检查等

class Array(object):      # 整体思想是通过对列表的操作方法进行包装来模拟数组的用法，注意从数组操作到列表操作的转换方法。

    def __init__(self, size=32):
        self._size = size
        self._items = [None] * size    # 注意定义定长列表的方法以及None的用法

    def __getitem__(self, index):
        return self._items[index]

    def __setitem__(self, index, value):
        self._items[index] = value       # 注意魔术方法__setitem__的用法，避免死循环

    def __len__(self):
        return self._size

    def clear(self, value=None):
        for i in range(len(self._items)):
            self._items[i] = value

    def __iter__(self):             # self._items本身是一个列表，可迭代，这里是生成器用法
        for item in self._items:
            yield item


def test_array():
    size = 10
    a = Array(size)
    a[0] = 1
    assert a[0] == 1
    assert len(a) == 10

# py.test array_and_list.py
L=[None]*5
print(len(L))

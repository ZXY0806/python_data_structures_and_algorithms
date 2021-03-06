# -*- coding: utf-8 -*-


def quicksort(array):
    if len(array) < 2:   # 递归出口，空数组或者只有一个元素的数组都是有序的
        return array
    else:
        pivot_index = 0    # 选择第一个元素作为主元 pivot
        pivot = array[pivot_index]
        less_part = [i for i in array[pivot_index+1:] if i <= pivot]
        great_part = [i for i in array[pivot_index+1:] if i > pivot]
        return quicksort(less_part) + [pivot] + quicksort(great_part)


def test_quicksort():
    import random
    seq = list(range(10))
    random.shuffle(seq)
    assert quicksort(seq) == sorted(seq)    # 用内置的sorted 『对拍』


def quicksort_inplace(array, beg, end):    # 注意这里我们都用左闭右开区间
    if beg < end:    # beg == end 的时候递归出口
        pivot = partition(array, beg, end)
        quicksort_inplace(array, beg, pivot)
        quicksort_inplace(array, pivot+1, end)


def partition(array, beg, end):
    pivot_index = beg
    pivot = array[pivot_index]
    left = pivot_index + 1
    right = end - 1    # 开区间，最后一个元素位置是 end-1     [0, end-1] or [0: end)，括号表示开区间

    while True:
        # 从左边找到比 pivot 大的
        while left <= right and array[left] < pivot:
            left += 1

        while right >= left and array[right] >= pivot:
            right -= 1

        if left > right:
            break
        else:
            array[left], array[right] = array[right], array[left]

    array[pivot_index], array[right] = array[right], array[pivot_index]
    return right   # 新的 pivot 位置

def nth_element(array, beg, end, k):     # 查找列表中起始位置之间第K大的元素
    pivot = partition(array, beg, end)
    if end - pivot == k:
        return array[pivot]
    if end - pivot > k:
        beg = pivot+1
        return nth_element(array, beg, end, k)
    if end - pivot < k:
        k -= end - pivot
        end = pivot
        return nth_element(array, beg, end, k)


def test_nth_element():
    l = [4, 2, 3, 5, 1]
    assert nth_element(l, 0, 5, 5) == 1
    l = [4, 2, 3, 5, 1]                     # nth_element()函数会改变l的元素顺序，因此这里重新定义l，方便断言
    assert nth_element(l, 2, 5, 2) == 3


def test_partition():
    l = [4, 1, 2, 8]
    assert partition(l, 1, len(l)) == 1
    l = [1, 2, 3, 4]
    assert partition(l, 2, len(l)) == 2
    l = [4, 3, 2, 1]



def test_quicksort_inplace():
    import random
    seq = list(range(10))
    random.shuffle(seq)
    sorted_seq = sorted(seq)
    quicksort_inplace(seq, 0, len(seq))
    assert seq == sorted_seq

import sys
if __name__ == '__main__':
    # sys.setrecursionlimit(1000000)
    test_partition()
    # test_quicksort_inplace()
    test_nth_element()




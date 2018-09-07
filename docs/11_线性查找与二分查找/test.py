# -*- coding:utf-8 -*-

number_list = [0, 1, 2, 3, 4, 5, 6, 7]

def linear_search_recusive(array, value):
    if len(array) == 0:
        return -1
    index = len(array)-1
    if array[index] == value:
        return index
    return linear_search_recusive(array[0:index], value)


assert linear_search_recusive(number_list, 5) == 5
assert linear_search_recusive(number_list, 8) == -1
assert linear_search_recusive(number_list, 7) == 7
assert linear_search_recusive(number_list, 0) == 0

index = len(number_list)
print(index)
print(number_list[0:7])    # 列表切片是左闭右开


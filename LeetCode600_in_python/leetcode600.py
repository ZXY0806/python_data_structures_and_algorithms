# -*- coding:utf-8 -*-
from collections import defaultdict
from random import randint


# 1. Two Sum
# 利用Pthon字典的特性，可以快速查找元素
class twosum_solution(object):
    def __init__(self, nums_list, target_value):
        self.nums_dict = {}
        for index, num in enumerate(nums_list):
            self.nums_dict[num] = index
        self.target_value = target_value
    def solve(self):
        index_list = []
        for key1 in self.nums_dict.keys():
            key2 = self.target_value - key1
            if key2 in self.nums_dict.keys():
                index_list.append(self.nums_dict[key1])
                index_list.append(self.nums_dict[key2])
                return index_list
        return None

def twosum_case():
    l = [1, 3, 5, 6, 9]
    s = twosum_solution(l, 9)
    print(s.solve())


# 改进twosum_solution,将两次遍历合并为一次
class twosum_solution_plus(object):
    def solve(self, nums_list, target_value):
        nums_dict = {}
        for index, num in enumerate(nums_list):
            sub = target_value - num
            if sub in nums_dict.keys():
                return [nums_dict[sub], index]
            else:
                nums_dict[num] = index

def twosum_case2():
    l = [1, 3, 5, 6, 9]
    s = twosum_solution_plus()
    print(s.solve(l, 9))


# 26. Remove Duplicates from Sorted Array(in place)
# 利用快慢指针思想
class removeduplicates(object):
    def solve(self, sorted_list):
        i = 0
        j = 1
        while j<len(sorted_list):
            if sorted_list[i] == sorted_list[j]:
                sorted_list.pop(j)
            else:
                i += 1
                j += 1
        return len(sorted_list)

def removeduplicates_case():
    l = [1, 1, 2, 4, 4, 5, 7, 7]
    s = removeduplicates()
    print(s.solve(l))
    print(l)

# 27. Remove Element
class removeelement(object):
    def solve(self, nums_list, value):
        i = 0
        while i < len(nums_list):
            if nums_list[i] != value:
                i += 1
            else:
                del nums_list[i]
                #nums_list.pop(i)
        return nums_list

def removeelement_case():
    l = [1, 1, 2, 3, 3, 4]
    s = removeelement()
    print(s.solve(l, 1))


# 35. Search Insert Position
# 使用二分思想缩减时间复杂度
class search_insert_position(object):
    def solve(self, sorted_list, value):
        start = 0
        end = len(sorted_list)-1
        med = int((start + end)/2)
        while med != end:
            if sorted_list[med] == value:
                return med
            elif sorted_list[med] > value:
                end = med
                med = int((start + end)/2)
            else:
                start = med + 1
                med = int((start + end)/2)
        return med

def search_insert_position_case():
    l = [2, 3, 5, 8, 14]
    s = search_insert_position()
    print(s.solve(l, 1))


# 3. Longest Substring Without Repeating Characters
# 注意查找的是最大无重复子串（连续的），利用滑动窗口思想
class length_of_longest_substring(object):
    def solve(self, s, res=0, left=0):
        dict = {}
        for index,value in enumerate(s):
            if value in dict.keys():
                if dict[value] >= left:
                    left = dict[value]+1
            dict[value] = index
            print(left, index)
            length = index - left + 1
            if length > res:
                res = length
        return res

def length_of_longest_substring_case():
    s1 = 'abcdabebcadf'
    s = length_of_longest_substring()
    print(s.solve(s1))


# 4. Median of Two Sorted Arrays(hard)
# 方法一：归并数组，当已选择的元素达到K，终止归并，时间复杂度为O(k);
# 方法二：利用二分查找思想，查找第K大的元素，假设数组A长度为m，数组B长度为n，则时间复杂度为O(log(m+n));
# 方法二具体思路：假设数组A、B，长度为m、n，m<n，定义函数findKthSmallest(indexA, m, indexB, n, k);
# 对K二分，需考虑边界值k=1、A或B为空、A的最小值大于B的最大值、B的最小值大于A的最大值。

class median_of_two_sorted_arrays(object):
    def solve_merged_search(self, list_A , list_B, k):
        if not list_A:
            return list_B[k-1]
        if not list_B:
            return list_A[k-1]
        if k == 1:
            return min(list_A[0], list_B[0])
        index_A = 0
        index_B = 0
        sum = 0
        while sum + 2 < k:
            # print(sum)
            if list_A[index_A] < list_B[index_B]:
                index_A += 1
            elif list_A[index_A] > list_B[index_B]:
                index_B += 1
            else: #list_A[index_A] == list_B[index_B]:
                index_A += 1
                index_B += 1
            if index_A >= len(list_A):
                return list_B[k - len(list_A) - 1]
            if index_B >= len(list_B):
                return list_A[k - len(list_B) - 1]
            sum = index_A + index_B
            if sum + 2 > k:
                return min(list_A[index_A], list_B[index_B])
        return max(list_A[index_A], list_B[index_B])
    def solve_binary_search(self, list_A, m, list_B, n): # 求中位数
        if (m + n) % 2 == 1:
            return self.findKthSmallest(list_A, m, list_B, n, int((m + n)/2)+1)
        else:
            return (self.findKthSmallest(list_A, m, list_B, n, int((m + n)/2)) +
                    self.findKthSmallest(list_A, m, list_B, n, int((m + n)/2) + 1))/2
    def findKthSmallest(self, list_A , m, list_B, n, k):  # m = len(list_A) < n = len(list_B)
        if m > n:
            return self.findKthSmallest(list_B, n, list_A, m, k)
        if not list_A:
            return list_B[k-1]
        if not list_B:
            return list_A[k-1]
        if k == 1:
            return min(list_A[0], list_B[0])
        index_A = min(int(k/2), m)
        index_B = k - index_A
        if list_A[index_A - 1] == list_B[index_B - 1]:
            return list_B[index_B - 1]
        elif list_A[index_A - 1] < list_B[index_B - 1]:
            list_A = list_A[index_A:]  # 切片中索引越界不会抛异常，直接按空返回结果,注意列表切片左闭右开原则
            m -= index_A
            list_B = list_B[:index_B]
            n = index_B
            k -= index_A
            return self.findKthSmallest(list_A, m, list_B, n, k)
        else:
            list_A = list_A[:index_A]
            m = index_A
            list_B = list_B[index_B:]
            n -= index_B
            k -= index_B
            return self.findKthSmallest(list_A, m, list_B, n, k)

def median_of_two_sorted_arrays_case():
    l1 = [1, 2, 3]
    l2 = [1, 1, 3, 8, 23]
    s = median_of_two_sorted_arrays()
    print(s.solve_binary_search(l1, len(l1), l2, len(l2)))
    print(s.solve_merged_search(l1, l2, 5))


# 5. Longest Palindromic Substring
# 方法一：遍历字符串，以每个字符为中心找最大回文子串，注意区分回文子串奇偶数情况；O(n^2)
# 方法二：马拉车算法O(n)
class longest_palindromic_substring(object):
    def solve_traverse(self, str, staindex=0, length=1):
        for i in range(len(str)-1):
            if str[i] == str[i+1]:
                left = i
                right = i + 1
                staindex, length = self.serach_palindromic_substring(str, left, right, staindex,length)
            if i - 1 > 0:
                left = i - 1
                right = i + 1
                staindex, length = self.serach_palindromic_substring(str, left, right, staindex, length)
        return str[staindex:staindex+length]

    def serach_palindromic_substring(self, str, left, right, staindex, length):
        while left >= 0 and right < len(str) and str[left] == str[right]:
            if right - left + 1 > length:
                length = right - left + 1
                staindex = left
            left -= 1
            right += 1
        return staindex, length

    def solve_manacher(self, str):
        new_str = '$#'
        for i in str:
            new_str += i + '#'
        print(new_str)
        p = defaultdict(lambda: 0)
        right = 1
        center = 1
        step = 0
        for i in range(1, len(new_str)):
            if i <= right:
                if p[2*center-i] < right-i+1:
                    pass
                else:
                    step = right - i
                    while i+step+1 < len(new_str) and i-step-1 > 0 and new_str[i-step-1] == new_str[i+step+1]:
                        step += 1
            else:
                while i+step+1 < len(new_str) and i-step-1 > 0 and new_str[i-step-1] == new_str[i+step+1]:
                    step += 1
            if step > right-center:
                right = i + step
                center = i
            p[i] = 1 + step
            step = 0
        print(right)
        print(center)
        print(p[center])
        return str[int(right/2-1)-p[center]+2:int(right/2)]

def longest_palindromic_substring_case():
    str = 'asdkgksdskaaks'
    s = longest_palindromic_substring()
    substr = s.solve_traverse(str)
    print(substr)
    substr1 = s.solve_manacher(str)
    print(substr1)


# 15. 3Sum
# 给定一个整型数组，找出所有不重复的三个数相加等于0的组合（组合成员按从小到大排序）
class three_sum(object):
    def solve(self, int_list):
        result = []
        int_list.sort()
        for index, num in enumerate(int_list):
            if num > 0:
                break
            if index > len(int_list) - 3:
                break
            if index > 0 and int_list[index] == int_list[index-1]:
                continue
            target_value = 0 - num
            left = index + 1
            right = len(int_list) - 1
            while left < right:
                if int_list[left] == int_list[index-1]:
                    left += 1
                    continue
                if int_list[left] + int_list[right] == target_value:
                    result.append((num, int_list[left], int_list[right]))
                    left += 1
                    right -= 1
                    continue
                if int_list[left] + int_list[right] > target_value:
                    right -= 1
                if int_list[left] + int_list[right] < target_value:
                    left += 1
        return result

def three_sum_case():
    L = [randint(-50, 60) for i in range(60)]
    s = three_sum()
    print(s.solve(L))


# 16. 给定一个整型数组，找出唯一的三个数相加与给定值最接近的组合，输出这三个数的和。
class three_sum_closet(object):
    def solve(self, int_list, target):
        diff = None
        int_list.sort()
        for index, num in enumerate(int_list):
            if index > len(int_list) - 3:
                break
            target_value = target - num
            left = index + 1
            right = len(int_list) - 1
            while left < right:
                sub_value = int_list[left]+int_list[right]-target_value
                sub_abs = abs(sub_value)
                if sub_value == 0:
                    diff = sub_abs
                    return diff
                if diff is None:
                    diff = sub_abs
                if sub_abs < diff:
                    diff = sub_abs
                if sub_value > 0:
                    right -= 1
                if sub_value < 0:
                    left += 1
        return diff

def three_sum_closet_case():
    L = [randint(-10, 10) for i in range(10)]
    s = three_sum_closet()
    print(sorted(L))
    print(s.solve(L, 15))



if __name__ == '__main__':
    three_sum_closet_case()

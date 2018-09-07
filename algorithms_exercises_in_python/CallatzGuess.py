# -*- coding:utf-8 -*-
#卡拉兹猜想：对于任何一个整数，如果它是偶数，把它砍掉一半；如果它是奇数，把3n+1砍掉一半。一直重复下去，最后一定能得到n=1
#题目：对给定的任一不超过1000的正整数N，求需要砍多少次才能得到n=1。

def callatzguess(num, n=0):
    if num % 2 == 0:
        num = num/2
    else:
        num = (3*num+1)/2
    n += 1
    if num == 1:
        return n
    else:
        return callatzguess(num, n)   # 必须加return（容易忘）

if __name__ == '__main__':
    m = callatzguess(3)
    print(m)

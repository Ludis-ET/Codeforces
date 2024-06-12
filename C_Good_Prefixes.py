from heapq import *
from math import ceil, gcd, log2
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right

def ii(): return int(input())
def ll():return list(map(int, input().split()))
def ss():return list(map(str, input().split()))



def solve():
    n = ii()
    a = ll()
    s=0
    m = float('-inf')
    res = 0
    for i in a:
        s += i
        m = max(m,i)
        if s == 2*m: 
            res += 1
    return res




    


# print(solve())

for _ in range(ii()):
    print(solve())

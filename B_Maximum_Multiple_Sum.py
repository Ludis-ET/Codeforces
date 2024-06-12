from heapq import *
from math import ceil, gcd, log2
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right

def ii(): return int(input())
def ll():return list(map(int, input().split()))
def ss():return list(map(str, input().split()))



def solve():
    n = ii()
    ans = 0
    cur = 0 
    for i in range(2, n + 1):
        # print(i,n//i, [i for i in range(i, (i * (n // i)) + 1, i)])
        x = sum([i for i in range(i, (i * (n // i)) + 1, i)])
        if x > cur:
            ans = i
            cur = x
    return ans


# for _ in range(int(input())):
#     print(3 if input() == '3' else 2)



    


# print(solve())

for _ in range(ii()):
    print(solve())

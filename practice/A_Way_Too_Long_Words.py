from heapq import *
from math import ceil, gcd, log2
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right

def ii(): return int(input())
def ll():return list(map(int, input().split()))
def ss():return list(map(str, input().split()))



def solve():
    s = input()
    n = len(s)
    if n <= 10:
        return s
    return str(s[0]) + str(n - 2) + str(s[-1])

    


# print(solve())

for _ in range(ii()):
    print(solve())

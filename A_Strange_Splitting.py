from heapq import *
from math import ceil, gcd, log2
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right

def ii(): return int(input())
def ll():return list(map(int, input().split()))
def ss():return list(map(str, input().split()))



def solve():
    n = ii()
    l = ll()

    if len(set(l)) == 1:
        return 'NO'
    print("YES")
    a = ['R'] * n
    a[1] = 'B'
    return ''.join(a)

    


# print(solve())

for _ in range(ii()):
    print(solve())

from heapq import *
from math import ceil, gcd, log2
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right

def ii(): return int(input())
def ll():return list(map(int, input().split()))
def ss():return list(map(str, input().split()))



def solve():
    a, b = ss()
    a = list(a)
    b = list(b)
    a[0], b[0] = b[0] , a[0]
    return str(''.join(a) + " " + ''.join(b))

    


# print(solve())

for _ in range(ii()):
    print(solve())

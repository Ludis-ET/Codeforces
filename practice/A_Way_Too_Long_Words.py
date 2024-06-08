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
    
    ans = ""
    ans += s[0]
    ans += str(n - 2)
    ans += s[-1]
    return ans

    


# print(solve())

for _ in range(ii()):
    print(solve())

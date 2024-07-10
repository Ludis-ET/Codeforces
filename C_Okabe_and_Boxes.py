import sys
import math
from heapq import *
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
 
def ii(): return int(sys.stdin.readline().strip())
def ll(): return list(map(int, sys.stdin.readline().strip().split()))
def ss(): return sys.stdin.readline().strip().split()
 
 
def solve():
    n = ii()
    ans = 0
    cur = 0
    for _ in range(2 * n):
        tmp = ss()
        if len(tmp) == 1 and cur > 1:
            ans += 1
            cur = 0
        elif len(tmp) == 2:
            cur += 1
    return ans
 
 
 
 
 
if __name__ == "__main__":
    print(solve())
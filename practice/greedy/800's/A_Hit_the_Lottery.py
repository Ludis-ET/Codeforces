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
    arr = [100, 20, 10, 5, 1]
    ans = 0
    for i in arr:
        if n >= i:
            ans += (n // i)
            n -= (n // i) * i
    return ans



if __name__ == "__main__":
    print(solve())
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
    arr = sorted(ll())[::-1]
    x = sum(arr)
    ans = 0
    y = 0
    while ans <= x:
        x -= arr[y]
        ans += arr[y]
        y += 1
    return y




if __name__ == "__main__":
    print(solve())
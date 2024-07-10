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
    a = ll()
    print(a[1] - a[0] ,a[-1] - a[0])
    for i in range(1,n - 1):
        x = a[i]
        p = a[i - 1]
        y = a[i + 1]
        print(min(x - p, y - x),max(x-a[0],a[-1]-x))
    print(a[-1] - a[-2] ,a[-1] - a[0])



if __name__ == "__main__":
    solve()
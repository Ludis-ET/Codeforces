import sys
import math
from heapq import *
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right

def ii(): return int(sys.stdin.readline().strip())
def ll(): return list(map(int, sys.stdin.readline().strip().split()))
def ss(): return sys.stdin.readline().strip().split()


def solve():
    arr = ll()
    s, d = 0, 0
    l, r = 0, len(arr) - 1
    n = 0
    while l <= r:
        if n % 2 == 0:
            if arr[l] >= arr[r]:
                s += arr[l]
                l += 1
            else:
                s += arr[r]
                r -= 1
        else:
            if arr[l] >= arr[r]:
                d += arr[l]
                l += 1
            else:
                d += arr[r]
                r -= 1
        n += 1
    return str(s) + " " + str(d)



if __name__ == "__main__":
    ii()
    print(solve())
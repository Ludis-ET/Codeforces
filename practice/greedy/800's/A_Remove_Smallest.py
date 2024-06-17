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
    arr = ll()
    arr.sort()
    for i in range(n - 1):
        if abs(arr[i] - arr[i + 1]) > 1:
            return "NO"
    return "YES"



if __name__ == "__main__":
    for _ in range(ii()):
        print(solve())
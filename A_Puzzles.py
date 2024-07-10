import sys
import math
from heapq import *
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right

def ii(): return int(sys.stdin.readline().strip())
def ll(): return list(map(int, sys.stdin.readline().strip().split()))
def ss(): return sys.stdin.readline().strip().split()


def solve():
    a, b = ll()
    arr = sorted(ll())
    ans = arr[-1] - arr[0]
    # print(arr)
    for i in range(len(arr) - a + 1):
        # print(arr[i + a - 1], arr[i])
        ans = min(ans, arr[i + a - 1] - arr[i])
    return ans




if __name__ == "__main__":
    print(solve())
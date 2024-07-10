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
    arr = ll()
    arr.sort()
    ans = float('-inf')
    cur = 1
    # print(arr, b)
    for i in range(1, a):
        if arr[i] - arr[i - 1] <= b:
            cur += 1
        else:
            cur = 1
        ans = max(ans, cur)
        # print(arr[i] - arr[i - 1],cur, ans)
    return a- ans if ans != float('-inf') else 0



if __name__ == "__main__":
    for _ in range(ii()):
        print(solve())
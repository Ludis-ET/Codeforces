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
    arr1 = ll()
    arr2 = ll()

    ans = [0] * n
    for i in arr1[1:]:
        ans [i - 1] = 1 if i > 0 else arr1[i - 1]
    for i in arr2[1:]:
        ans [i - 1] = 1 if i > 0 else arr1[i - 1]
    return "I become the guy." if not 0 in ans else "Oh, my keyboard!"
    



if __name__ == "__main__":
    # for _ in range(ii()):
    print(solve())
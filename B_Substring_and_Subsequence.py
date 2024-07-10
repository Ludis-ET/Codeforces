import sys
import math
from heapq import *
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right

def ii(): return int(sys.stdin.readline().strip())
def ll(): return list(map(int, sys.stdin.readline().strip().split()))
def ss(): return sys.stdin.readline().strip().split()


def solve():
    a = input().strip()
    b = input().strip()
    n = len(a)
    m = len(b)
    ans = n + m
    for i in range(m):
        j = i
        for c in a:
            if j < m and c == b[j]:
                j += 1
        ans = min(ans, n + m - (j - i))
    return ans



if __name__ == "__main__":
    for _ in range(ii()):
        print(solve())
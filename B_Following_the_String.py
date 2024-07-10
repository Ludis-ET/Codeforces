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
    l = ll()
    a = [0] * n
    c = [chr(97 + i) for i in range(26)]
    ans = ''

    for i in l:
        ans += c[a[i]]
        a[i] += 1
    return ans




if __name__ == "__main__":
    for _ in range(ii()):
        print(solve())
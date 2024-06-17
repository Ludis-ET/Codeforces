import sys
import math
from heapq import *
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right

def ii(): return int(sys.stdin.readline().strip())
def ll(): return list(map(int, sys.stdin.readline().strip().split()))
def ss(): return sys.stdin.readline().strip().split()


def solve():
    n, m = ll()
    a, b = min(n, m), max(n, m)
    return (b // 2) * a + (a // 2) * (b % 2 != 0)



if __name__ == "__main__":
    # for _ in range(ii()):
    print(solve())

import sys
import math
from heapq import *
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right

def ii(): return int(sys.stdin.readline().strip())
def ll(): return list(map(int, sys.stdin.readline().strip().split()))
def ss(): return sys.stdin.readline().strip().split()


def solve():
    x, n, m = map(int, input().split())
    while n > 0 and x > 20:
        x = (x // 2) + 10
        n -= 1

    x -= 10 * m
    
    return 'YES' if x <= 0 else 'NO'



if __name__ == "__main__":
    for _ in range(ii()):
        print(solve())
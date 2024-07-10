import sys
import math
from heapq import *
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right

def ii(): return int(sys.stdin.readline().strip())
def ll(): return list(map(int, sys.stdin.readline().strip().split()))
def ss(): return sys.stdin.readline().strip().split()


def solve():
    a = sorted(ll())
    ans = 0
    for i in a:
        ans += abs(i - a[-2])
    return ans



if __name__ == "__main__":
    for _ in range(ii()):
        print(solve())
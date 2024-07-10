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
    s = list(i for i in input())
    # print(s)
    ans = 0
    for i in range(2, len(s)):
        if s[i - 2] == 'm' and s[i - 1] == 'a' and s[i] == 'p':
            ans += 1
            s[i] = 'x'
        elif s[i - 2] == 'p' and s[i - 1] == 'i' and s[i] == 'e':
            ans += 1
            s[i - 2] = 'y'
    return ans




if __name__ == "__main__":
    for _ in range(ii()):
        print(solve())
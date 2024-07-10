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
    a = ll()
    a.sort(key=lambda x: x % 2)
    ans = 0
    for i in range(n):
        for j in range(i + 1, n):
            if math.gcd(a[i], 2 * a[j]) > 1:
                ans += 1
    
    return ans




if __name__ == "__main__":
    for _ in range(ii()):
        print(solve())
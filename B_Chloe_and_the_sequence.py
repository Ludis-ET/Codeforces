import sys
import math
from heapq import *
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right

def ii(): return int(sys.stdin.readline().strip())
def ll(): return list(map(int, sys.stdin.readline().strip().split()))
def ss(): return sys.stdin.readline().strip().split()


def solve(n, k):
    if n == 1:
        return 1
    
    len_previous = (1 << (n - 1)) - 1  # Length of sequence at n-1
    if k <= len_previous:
        return solve(n - 1, k)
    elif k == len_previous + 1:
        return n
    else:
        return solve(n - 1, 2 * len_previous + 2 - k)



if __name__ == "__main__":
    n, k = ll()
    print(solve(n,k))
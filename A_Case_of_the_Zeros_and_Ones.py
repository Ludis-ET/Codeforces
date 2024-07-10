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
    arr = input()
    a = arr.count('0')
    b = arr.count('1')
    return n - (min(a,b) * 2)



if __name__ == "__main__":
    print(solve())
import sys
import math
from heapq import *
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right

def ii(): return int(sys.stdin.readline().strip())
def ll(): return list(map(int, sys.stdin.readline().strip().split()))
def ss(): return sys.stdin.readline().strip().split()


def solve():
    la, lb = ll()
    ra, rb = ll()

    if la > lb:
        la, lb, ra, rb = lb, la, rb, ra
    if la < lb and rb < ra:
        return "NO"
    else:
        return 'YES'



if __name__ == "__main__":
    for _ in range(ii()):
        print(solve())
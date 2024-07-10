import sys
import math
from heapq import *
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right

def ii(): return int(sys.stdin.readline().strip())
def ll(): return list(map(int, sys.stdin.readline().strip().split()))
def ss(): return sys.stdin.readline().strip().split()


def solve():
    a = input()
    prev = -1
    for i in a:
        if i not in {'1','4'} or (i == '4' and prev not in [0,1]):
            return 'NO'
        if i == '4':
            prev += 1
        else:
            prev = 0
    return 'YES'



if __name__ == "__main__":
    print(solve())
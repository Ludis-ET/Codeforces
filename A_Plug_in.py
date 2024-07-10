import sys
import math
from heapq import *
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right

def ii(): return int(sys.stdin.readline().strip())
def ll(): return list(map(int, sys.stdin.readline().strip().split()))
def ss(): return sys.stdin.readline().strip().split()



def solve():
    s = input()
    stack = []
    for i in s:
        if stack and stack[-1] == i:
            stack.pop()
            continue
        stack.append(i)
    return "".join(stack)
        
    



if __name__ == "__main__":
    print(solve())
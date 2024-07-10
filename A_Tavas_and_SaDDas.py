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
    def tmp():
        ans = []
        
        def dfs(cur, lim):
            if cur > lim:
                return
            ans.append(cur)
            dfs(cur * 10 + 4, lim)
            dfs(cur * 10 + 7, lim)
        
        dfs(0, 10**9)
        return ans
    
    ans = tmp()
    ans.sort()
    
    return ans.index(n)



if __name__ == "__main__":
    print(solve())
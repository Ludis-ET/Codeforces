from collections import defaultdict
from collections import Counter
from math import gcd

def jj(): return int(input())
def ff():return list(map(int, input().split()))



def solve():
    n = jj()
    a = ff()
    b = ff()
    m = jj()
    d = ff()

    stack = 0
    e = []
    for i, j in zip(a, b):
        if i != j:
            e.append(j)
    
    s = n - len(e)
    first = Counter(e)
    second = set(b)
    cnt = Counter(d)
    for i in d:
        if i not in second:
            stack = 1
        elif stack > 0:
            s += first[i] > 0
            cnt[i] -= 1
            stack = 0
        elif first[i] > 0 and cnt[i] > 0:
            s += 1
            cnt[i] -= 1
            first[i] -= 1
    return "YES" if s == n and stack == 0 else "NO"


# print(solve())

for _ in range(jj()):
    print(solve())

from math import gcd

def good(b):
    g = gcd(b[0], b[1])
    for i in range(1, len(b) - 1):
        cur_gcd = gcd(b[i], b[i + 1])
        if g > cur_gcd:
            return False
        g = cur_gcd
    return True

def solve():
    n = int(input())
    a = list(map(int, input().split()))

    g = -1
    to_del = -1
    for i in range(n - 1):
        cur_gcd = gcd(a[i], a[i + 1])
        if cur_gcd < g:
            to_del = i
            break
        g = cur_gcd

    if to_del == -1:
        return True

    b0 = a.copy()
    b1 = a.copy()
    b2 = a.copy()

    if to_del > 0:
        b0.pop(to_del - 1)
    b1.pop(to_del)
    if to_del < n - 1:
        b2.pop(to_del + 1)

    return good(b0) or good(b1) or good(b2)

t = int(input())
for _ in range(t):
    print("YES" if solve() else "NO")

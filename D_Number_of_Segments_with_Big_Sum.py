n, s = map(int, input().split())
arr = list(map(int, input().split()))

x = 0, L = 0
for R = 0..n-1
    x += a[R]
    while x > s:
        x -= a[L]
        L++
    res += R - L + 1

print(ans)
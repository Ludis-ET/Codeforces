n, s = map(int, input().split())
arr = list(map(int, input().split()))

total = 0
ans = 0
l = 0
for r in range(n):
    total += arr[r]
    while total > s:
        total -= arr[l]
        l += 1
    ans += r - l + 1

print(ans)
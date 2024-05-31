n, s = map(int, input().split())
arr = list(map(int, input().split()))

total = 0
ans = float('inf')
l = 0
for r in range(n):
    total += arr[r]
    while total>= s:
        ans = min(ans, r - l + 1)
        total -= arr[l]
        l += 1
print(ans if ans != float('inf') else -1)
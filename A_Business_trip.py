k = int(input())
arr = sorted(map(int, input().split()))[::-1]
ans = 0
i = 0
while ans < k and i < 12:
    ans += arr[i]
    i += 1
print(i if ans >= k else -1)
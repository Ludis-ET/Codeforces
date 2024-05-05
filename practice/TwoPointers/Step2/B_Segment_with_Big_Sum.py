n, s = map(int, input().split())
arr = list(map(int, input().split()))

l = 0
total = 0
min_length = n

for r in arr:
    total += r
    # print(total)
    while total >= s:
        total -= arr[l]
        l += 1
    min_length = min(min_length, r - l + 1)
    # print(total)

print(min_length)

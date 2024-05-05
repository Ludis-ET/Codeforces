n, s = map(int, input().split())
arr = list(map(int, input().split()))

left = 0
sum_segment = 0
max_length = 0

for right in range(n):
    sum_segment += arr[right]
    while sum_segment > s:
        sum_segment -= arr[left]
        left += 1
    max_length = max(max_length, right - left + 1)

print(max_length)

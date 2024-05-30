t = int(input())
arr = [0] * 3
for _ in range(t):
    a, b, c = map(int, input().split())
    arr[0] += a
    arr[1] += b
    arr[2] += c
print("YES" if arr == [0] * 3 else "NO")
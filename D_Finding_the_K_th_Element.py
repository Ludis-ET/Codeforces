n, k = map(int, input().split())

ans = 1
for i in range(1, n):
    ans *= 2


temp = (ans + 1) // 2

if k > temp:
    k = ans - k

for i in range(n, 0, -1):
    if k % (2 ** (i - 1)) == 0:
        print(i)
        break

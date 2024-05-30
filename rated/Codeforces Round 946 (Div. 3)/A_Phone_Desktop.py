for _ in range(int(input())):
    x, y = map(int, input().split())
    ans = (y + 1)// 2
    mx = (7 * (y // 2)) + ((y % 2 != 0) * 11)
    x -= mx
    while x > 0:
        ans += 1
        x -= 15
    print(ans)

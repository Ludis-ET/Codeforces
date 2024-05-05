t = int(input())
n, k = map(int, input().split())
s = str(input())

for _ in range(t):
    l, r = 0, 0
    ans = n
    while r < n:
        x = r - l + 1
        cnt = 0
        while x <= k and r < n:
            # print(x, l, r, ans, cnt)
            if s[r] == "W": cnt += 1
            r += 1
            x = r - l + 1
        
        if x - 1 == k: ans = min(cnt, ans)
        l += 1
        r = l
    print(ans)

for _ in range(int(input())):
    n = int(input())
    s = str(input())
    ans, i = 0, 0
    
    while i < n and ans <= n / 3 and ans >= 0:
        ans += 1 if s[i] == "T" else -1
        i += 1
    
    print("YES" if ans == n / 3 else "NO")



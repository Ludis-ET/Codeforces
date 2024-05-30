for _ in range(int(input())):
    n = int(input())
    s = str(input())
    r = sorted(list(set(s)))
    table = {}
    for i in range(len(r)):
        table[r[i]] = i

    ans = ""
    for i in range(n):
        ans += r[len(r) - table[s[i]] - 1]
    print(ans)



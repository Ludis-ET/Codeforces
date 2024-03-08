testcase = int(input())
for _ in range(testcase):
    e = input().split("+")
    ans = 0
    for a in e:
        ans += int(a)
    print(ans)
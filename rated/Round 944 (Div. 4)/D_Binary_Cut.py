t = int(input())

for _ in range(t):
    s = input()
    s += "4"
    e = s.count('01')
    r = 0
    for i in range(len(s) - 1):
        r += s[i] != s[i + 1]
    print(r - e)
s = str(input())
m = "hello"
l, r = 0, 0
while l < len(m) and r < len(s):
    if m[l] == s[r]:
        l += 1
    r += 1
print("YES" if l == 5 else "NO")
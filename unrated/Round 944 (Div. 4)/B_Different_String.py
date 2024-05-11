t = int(input())

for _ in range(t):
    s = input()

    if len(set(s)) == 1:
        print("NO")
    else:
        print("YES")
        rearranged = s[1:] + s[0]
        print(rearranged)

# 2
# aaabbb
# ab

# YES
# ababab
# NO
testcase = int(input())
for _ in range(testcase):
    a = int(input())
    b = str(input())
    l, r = 0, len(b) - 1
    while a > 0 and r != l and int(b[l]) + int(b[r]) == 1:
        a -= 2
        l += 1
        r -= 1
    print(a)
# 8
# 11100101
#  - 8
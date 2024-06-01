a1, a2 = map(int, input().split())

ans = 0

while a1 > 0 and a2 > 0 and not (a1 == 1 and a2 == 1):
    
    if a1 > a2:
        a1, a2 = a2, a1
    a1 += 1
    a2 -= 2
    
    ans += 1

print(ans)

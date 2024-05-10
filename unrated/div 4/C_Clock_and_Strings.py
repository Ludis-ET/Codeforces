t = int(input())
for _ in range(t):
    a,b,c,d = map(int, input().split())
    f,s = max(a,b) , max(c,d)
    e,g = min(a,b) , min(c,d)
    if (s > f and g < f and g > e) or (f > s and g < e and e > g):
        print("YES")
    else:
        print("NO")



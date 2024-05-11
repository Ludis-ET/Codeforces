t = int(input())
for _ in range(t):
    a,b,c,d = map(int, input().split())
    e = 0
    no = False
    for i in range(1, 13):
        if i == a or i == b:
            if e == 1:
                print("NO")
                no = True
                break
            else:
                e = 1
        elif i == c or i == d:
            if e == 2:
                print("NO")
                no = True
                break
            else:
                e = 2
    if not no:
        print("YES")




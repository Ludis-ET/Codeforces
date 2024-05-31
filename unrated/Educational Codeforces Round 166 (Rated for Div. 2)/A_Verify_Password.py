for _ in range(int(input())):
    n = int(input())
    pas = str(input())
    
    dig = []
    l = []
    for i in pas:
        if i.isdigit():
            dig.append(i)
        elif i.isalpha():
            l.append(i)
    
    if dig != sorted(dig) or l != sorted(l):
        print("NO")
        continue
    
    seen = False
    ans = True
    for i in pas:
        if i.isalpha():
            seen = True
        elif i.isdigit() and seen:
            ans = False
            break
    
    if ans:
        print("YES")
    else:
        print("NO")


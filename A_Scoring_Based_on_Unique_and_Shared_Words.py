for _ in range(int(input())):
    n = int(input())
    a = input().split()
    b = input().split()
    c = input().split()
    
    cnt = {}
    

    for i in a:
        if i in cnt:
            cnt[i] += 1
        else:
            cnt[i] = 1
            
    for i in b:
        if i in cnt:
            cnt[i] += 1
        else:
            cnt[i] = 1
            
    for i in c:
        if i in cnt:
            cnt[i] += 1
        else:
            cnt[i] = 1

    p1 = 0
    p2 = 0
    p3 = 0


    for i in a:
        if cnt[i] == 1:
            p1 += 3
        elif cnt[i] == 2:
            p1 += 1
    

    for i in b:
        if cnt[i] == 1:
            p2 += 3
        elif cnt[i] == 2:
            p2 += 1
    

    for i in c:
        if cnt[i] == 1:
            p3 += 3
        elif cnt[i] == 2:
            p3 += 1
    
    print(p1, p2, p3)

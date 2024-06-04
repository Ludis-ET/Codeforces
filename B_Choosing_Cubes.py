for _ in range(int(input())):
    n, f, k = map(int, input().split())
    a = list(map(int, input().split()))

    ff = a[f - 1]
    
    ss = sorted(a, reverse=True)
    
    gc = sum(1 for x in ss if x > ff)
    fv = ss.count(ff)
    
    if gc >= k:
        print("NO")
    elif gc + fv <= k:
        print("YES")
    else:
        print("MAYBE")

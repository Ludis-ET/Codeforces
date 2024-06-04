for _ in range(int(input())):
    n, m = map(int, input().split())
    p = input()
    

    cnt = {ch: 0 for ch in 'ABCDEFG'}
    for i in p:
        cnt[i] += 1

    
    ans = 0
    for i in 'ABCDEFG':
        if cnt[i] < m:
            ans += m - cnt[i]

    print(ans)

for _ in range(int(input())):
    n = int(input())
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))

    x = set(arr1)
    y = arr2[-1]
    op = [float('inf'), 0]
    l = float('inf')
    for i in range(n):
        ans = 1
        z = abs(arr1[i] - y)
        if z < op[0]:
            op = [z, arr1[i]]
            print(abs(y - arr1[i]), abs(arr1[i] - arr2[i]))
            if abs(y - arr1[i]) < abs(arr1[i] - arr2[i]):
                arr1[i] += y - arr1[i]
                ans += abs(arr1[i] - arr2[i])
            else:
                ans += abs(y - arr1[i])
        l = min(l, ans)

    arr1.append(y)
    print(arr1, arr2, l)


    for i, j in zip(arr1, arr2):
        l += abs(i - j)

    print(l)

            

t = int(input())
 
for i in range(t):
    n, m = map(int, input().split())
    l = max(0, n - m)
    r = n + m
    x = (l ^ r).bit_length()
    print(l | r | ((1 << x) - 1))
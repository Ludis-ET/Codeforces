test = int(input())

while test > 0:
    test -= 1
    floor = 1
    p, x = map(int, input().split())
    
    if p > 2:
        while not ((((floor - 1) * x) + 3) <= p <= ((floor * x) + 2)): 
            floor += 1
        print(floor + 1)
    else:
        print(floor)

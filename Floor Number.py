test = int(input())

while test > 0:
    test -= 1
    floor = 1
    p, x = map(int, input().split())
    
    if p > 2:
        counter = 0
        while not (((counter * x) + 3) <= p <= ((floor * x) + 2)):
            floor += 1
            counter += 1
        print(floor + 1)
    else:
        print(floor)

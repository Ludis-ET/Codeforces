t = int(input())

for _ in range(t):
    s = input()
    print(s.count('10') + 1 + max(0, s.count('01') - 1))
from collections import defaultdict

a, b = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

table1 = defaultdict(int)
table2 = defaultdict(int)

for i in arr1:
    table1[i] += 1

for i in arr2:
    table2[i] += 1
 
total = 0
for k, v in table1.items():
    total += table2[k] * v

print(total)
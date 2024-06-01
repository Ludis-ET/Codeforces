n, k = map(int, input().split())

a =[i for i in range(1, n + 1) if i % k == 0]
b =[i for i in range(1, n + 1) if i % k != 0]


ans = []
l, r = 0, 0 
i = 1
while l < len(a) and r < len(b):
    if i > 0 and i <= k:
        ans.append(b[r])
        r += 1
        i += 1
        continue
    if i > k and i <= 2 * k:
        ans.append(a[l])
        l += 1
        i += 1
        continue
    if i == 2 * k:
        i = 1

if l < len(a):
    ans.extend(a[l:])

if r < len(b):
    ans.extend(b[r:])

print(*ans)



"""
A permutation p
 is an ordered set of integers p1,  p2,  …,  pn
, consisting of n
 distinct positive integers not larger than n
. We denote n
 as the length of the permutation p1,  p2,  …,  pn
.

Your task is to find such a permutation p
 of length n
, such that the group of numbers |p1−p2|,|p2−p3|,…,|pn−1−pn|
 has exactly k
 distinct elements.

Input
The single line of the input contains two space-separated positive integers n
 and k
 (1≤k<n≤105
).

Output
Print n
 integers forming the permutation. If there are multiple answers, print any of them.

Examples
inputCopy
3 2
outputCopy
1 3 2
inputCopy
3 1
outputCopy
1 2 3
inputCopy
5 2
outputCopy
1 3 2 4 5
Note
By |x|
 we denote the absolute value of number x
.




"""
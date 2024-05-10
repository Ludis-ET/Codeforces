def count_lattice_points(r):
    count = 0
    x = -r
    while x <= r:
        y = 0
        while y * y <= r * r - x * x:
            y += 1
        count += 2 * y - 1
        x += 1
    return count

t = int(input())
for _ in range(t):
    r = int(input())
    print(count_lattice_points(r))

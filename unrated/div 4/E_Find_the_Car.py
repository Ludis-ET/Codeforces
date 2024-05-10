def find_time(points, times, query):
    low = 0
    high = len(points) - 1

    while low < high:
        mid = (low + high) // 2
        if points[mid] < query:
            low = mid + 1
        else:
            high = mid

    if low == 0:
        return times[0] * query // points[0]
    else:
        return times[low - 1] + (times[low] - times[low - 1]) * (query - points[low - 1]) // (points[low] - points[low - 1])

t = int(input())

for _ in range(t):
    n, k, q = map(int, input().split())
    points = list(map(int, input().split()))
    times = list(map(int, input().split()))

    for _ in range(q):
        query = int(input())
        print(find_time(points, times, query), end=" ")
    print()

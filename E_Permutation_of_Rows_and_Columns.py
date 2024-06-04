def solve_test_case(n, m, a, b):
    position_a = {}  # Dictionary to store positions of elements in matrix a

    # Populate position_a with indices of elements in matrix a
    for i in range(n):
        for j in range(m):
            position_a[a[i][j]] = (i, j)

    # Check if elements in matrix b match their positions in matrix a
    for i in range(n):
        for j in range(m):
            if b[i][j] != a[position_a[b[i][j]][0]][position_a[b[i][j]][1]]:
                return "NO"  # Found a mismatch

    return "YES"  # All elements match

# Read input
t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]
    b = [list(map(int, input().split())) for _ in range(n)]

    # Solve the test case
    print(solve_test_case(n, m, a, b))

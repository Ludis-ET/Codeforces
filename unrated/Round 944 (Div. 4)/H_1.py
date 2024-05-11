def can_alice_win(n, grid):
    # Iterate over each column
    for j in range(n):
        # Extract values from the column
        values = [grid[i][j] for i in range(3)]
        # Sort the values
        values.sort()

        # Check if the middle row will have all 1s after sorting
        if values[1] <= 0:
            # If the middle value is negative or 0, Alice cannot win
            return "NO"

    return "YES"

def check_alice_win(t, test_cases):
    for _ in range(t):
        n = int(input())
        grid = [list(map(int, input().split())) for _ in range(3)]
        print(can_alice_win(n, grid))

# Input
t = int(input())
check_alice_win(t, range(t))

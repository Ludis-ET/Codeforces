import heapq

def lexicographically_smallest_array(n, arr):
    buckets = [[] for _ in range(1000000000 // 4 + 1)]  # Using buckets based on the maximum possible value after XOR

    # Place elements into buckets based on their values after XOR
    for num in arr:
        buckets[num // 4].append(num)

    # Iterate through each bucket
    for bucket in buckets:
        if not bucket:
            continue

        # Create a priority queue to efficiently find the minimum value within the bucket
        min_heap = bucket[:]
        heapq.heapify(min_heap)

        # Apply swapping logic within each bucket
        for i in range(len(bucket)):
            min_valid = min_heap[0]
            min_valid_index = bucket.index(min_valid)
            if min_valid_index != i:
                bucket[i], bucket[min_valid_index] = bucket[min_valid_index], bucket[i]
                # Update the priority queue after swapping
                min_heap.remove(min_valid)
                heapq.heapify(min_heap)

    # Concatenate the sorted buckets to form the resulting array
    result = []
    for bucket in buckets:
        result.extend(bucket)

    return result

def process_test_cases(t, test_cases):
    for case in test_cases:
        n = case[0]
        arr = case[1]
        result = lexicographically_smallest_array(n, arr)
        print(" ".join(map(str, result)))

# Input
t = int(input())
test_cases = []
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    test_cases.append((n, arr))

# Output
process_test_cases(t, test_cases)

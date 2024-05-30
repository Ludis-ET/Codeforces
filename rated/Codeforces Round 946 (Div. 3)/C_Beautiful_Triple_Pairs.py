def count_beautiful_pairs(t, test_cases):
    results = []
    for case in test_cases:
        n, a = case
        
        # Dictionary to count full triples
        full_triples = {}
        
        # Dictionaries to count partial triples with one wildcard
        count_1 = {}
        count_2 = {}
        count_3 = {}
        
        # Generate all triples and fill dictionaries
        for i in range(n - 2):
            triple = (a[i], a[i + 1], a[i + 2])
            
            if triple in full_triples:
                full_triples[triple] += 1
            else:
                full_triples[triple] = 1
            
            # Count patterns with one wildcard
            p1 = ('*', a[i + 1], a[i + 2])
            p2 = (a[i], '*', a[i + 2])
            p3 = (a[i], a[i + 1], '*')
            
            if p1 in count_1:
                count_1[p1] += 1
            else:
                count_1[p1] = 1
            
            if p2 in count_2:
                count_2[p2] += 1
            else:
                count_2[p2] = 1
            
            if p3 in count_3:
                count_3[p3] += 1
            else:
                count_3[p3] = 1
        
        beautiful_pairs = 0
        
        # Calculate the number of beautiful pairs
        for triple in full_triples:
            count = full_triples[triple]
            
            p1 = ('*', triple[1], triple[2])
            p2 = (triple[0], '*', triple[2])
            p3 = (triple[0], triple[1], '*')
            
            if p1 in count_1:
                beautiful_pairs += count * count_1[p1]
            if p2 in count_2:
                beautiful_pairs += count * count_2[p2]
            if p3 in count_3:
                beautiful_pairs += count * count_3[p3]
        
        # Each pair is counted twice (once for each direction), so divide by 2
        beautiful_pairs //= 2
        
        results.append(beautiful_pairs)
    
    return results

# Read input
t = int(input())
test_cases = []
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    test_cases.append((n, a))

# Process and print output
results = count_beautiful_pairs(t, test_cases)
for result in results:
    print(result)

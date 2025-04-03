def count_segments_after_removals(houses, queries):

    def count_segments(houses):
        segments = 0
        prev = None
        for h in houses:
            if prev is None or h != prev + 1:
                segments += 1
            prev = h
        return segments
    
    house_set = set(houses)
    results = []
    
    for query in queries:
        house_set.remove(query)
        results.append(count_segments(house_set))
    
    return results

# Example usage
houses = [1, 5, 6, 8, 10]
queries = [5, 10, 1]
print(count_segments_after_removals(houses, queries))  # Output: [3, 3, 2]

from itertools import combinations

def valid_subset(subset, K):
    for i in range(len(subset)):
        for j in range(i + 1, len(subset)):
            if abs(subset[i] - subset[j]) == K:
                return False
    return True

def count_and_print_non_friend_subsets(N, K, AR):
    count = 0
    valid_subsets = []
    for r in range(1, N + 1):
        for subset in combinations(AR, r):
            if valid_subset(subset, K):
                valid_subsets.append(subset)
                count += 1
    print(f"Total number of valid subsets: {count}")
    for subset in valid_subsets:
        print(subset)

# Test cases
print("Test case 1:")
count_and_print_non_friend_subsets(5, 2, [8, 7, 10, 6, 5])
print("\nTest case 2:")
count_and_print_non_friend_subsets(2, 3, [6, 9])



# from itertools import combinations

# def valid_subset(subset, K):
#     for i in range(len(subset)):
#         for j in range(i + 1, len(subset)):
#             if abs(subset[i] - subset[j]) == K:
#                 return False
#     return True

# def count_non_friend_subsets(N, K, AR):
#     count = 0
#     for r in range(1, N + 1):
#         for subset in combinations(AR, r):
#             if valid_subset(subset, K):
#                 count += 1
#     return count

# # Test cases
# print(count_non_friend_subsets(5, 2, [8, 7, 10, 6, 5]))  # Output should be 14
# print(count_non_friend_subsets(2, 3, [6, 9]))            # Output should be 2

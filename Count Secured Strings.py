# https://www.fastprep.io/problems/amazon-count-secured-strings


def amazon_count_secured_strings(s1: str, s2: str) -> int:
    MOD = 10**9 + 7
    n = len(s1)
    count = 0
    
    def get_subsequences(s):
        subsequences = []
        for i in range(1, 1 << len(s)):
            sub = ''.join(s[j] for j in range(len(s)) if (i & (1 << j)))
            subsequences.append(sub)
        return subsequences
    
    subsequences = get_subsequences(s1)
    subsequences.sort()
    
    comparison_results = []
    
    for sub in subsequences:
        if sub > s2:
            count = (count + 1) % MOD
            comparison_results.append((sub, "Greater"))
        elif sub == s2:
            comparison_results.append((sub, "Equal"))
        else:
            comparison_results.append((sub, "Smaller"))
    
    print("Subsequence | Lexicographical Comparison with t")
    print("------------------------------------------------")
    for sub, result in comparison_results:
        print(f"{sub:<12} | {result}")
    
    return count

# Example test cases
print("Output:", amazon_count_secured_strings("aba", "ab"))  # Output: 3
print("Output:", amazon_count_secured_strings("bab", "ab"))  # Output: 5

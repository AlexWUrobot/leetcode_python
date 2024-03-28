# https://www.fastprep.io/problems/amazon-find-number-of-ways-to-group-parcels

def numberOfWaysToGroupParcels(weight, wt):
    MOD = 10**9 + 7
    
    # Count occurrences of each weight
    weight_count = {}
    for w in weight:
        weight_count[w] = weight_count.get(w, 0) + 1

    # Initialize result
    result = 0
    
    # Iterate over each weight
    for w in weight_count:
        # Check if there exists another weight with absolute difference equal to wt
        if w - wt in weight_count:
            # Calculate the number of ways to choose pairs
            result += (weight_count[w] * weight_count[w - wt]) % MOD

    # Divide by 2 to account for the double counting of pairs
    result //= 2
    
    return result % MOD

# Test the function
weight = [4, 5, 5, 4, 4, 5, 2, 3]
wt = 1
print(numberOfWaysToGroupParcels(weight, wt))  # Output: 6

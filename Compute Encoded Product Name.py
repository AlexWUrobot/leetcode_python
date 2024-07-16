# https://www.fastprep.io/problems/amazon-compute-encoded-product-name


def computeEncodedProductName(nameString: str) -> str:
    n = len(nameString)
    
    if n % 2 == 0:
        # Even length
        half_len = n // 2
        first_half = nameString[:half_len]
        sorted_first_half = ''.join(sorted(first_half))
        encoded_name = sorted_first_half + sorted_first_half[::-1]
    else:
        # Odd length
        half_len = n // 2
        first_half = nameString[:half_len]
        middle_char = nameString[half_len]
        sorted_first_half = ''.join(sorted(first_half))
        encoded_name = sorted_first_half + middle_char + sorted_first_half[::-1]
    
    return encoded_name

# Example usage:
nameString1 = "yxxy"
encoded_name1 = computeEncodedProductName(nameString1)
print(encoded_name1)  # Output: "xyyx"

nameString2 = "ded"
encoded_name2 = computeEncodedProductName(nameString2)
print(encoded_name2)  # Output: "ded"

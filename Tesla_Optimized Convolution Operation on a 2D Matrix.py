# Q2: Optimized Convolution Operation on a 2D Matrix


# Explanation of the Algorithm:
# The function slides a k x k kernel over the matrix and computes the sum of element-wise multiplications.
# We iterate over the matrix such that the kernel stays within bounds.
# The result matrix has dimensions (m-k+1) x (n-k+1), as each valid position of the kernel produces one output.


from typing import List

def convolution_2d(matrix: List[List[int]], kernel: List[List[int]]) -> List[List[int]]:
    m, n = len(matrix), len(matrix[0])  # Dimensions of the input matrix
    k = len(kernel)  # Assuming square kernel (k x k)
    
    output_size = m - k + 1  # The size of the output matrix
    result = [[0] * output_size for _ in range(output_size)]  # Initialize result matrix with zeros

    # Slide the kernel over the matrix
    for i in range(output_size):
        for j in range(output_size):
            conv_sum = 0  # Accumulator for the convolution sum
            
            # Apply kernel to the corresponding region in the matrix
            for ki in range(k):
                for kj in range(k):
                    conv_sum += matrix[i + ki][j + kj] * kernel[ki][kj]
            
            result[i][j] = conv_sum  # Store the convolution result

    return result

# Test case
M = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

K = [
    [1, 0],
    [0, -1]
]

output = convolution_2d(M, K)
for row in output:
    print(row)


# Time Complexity O(MxNxK^2)
# Space Complexity O((M-K+1) x (N-K+1))


# faster version =====================================================================================================

import numpy as np

def convolution_2d_numpy(matrix, kernel):
    matrix = np.array(matrix)
    kernel = np.array(kernel)
    
    m, n = matrix.shape
    k, _ = kernel.shape

    output_size = m - k + 1
    result = np.zeros((output_size, output_size))

    # Using NumPy slicing to speed up element-wise multiplication
    for i in range(output_size):
        for j in range(output_size):
            result[i, j] = np.sum(matrix[i:i+k, j:j+k] * kernel)

    return result.tolist()

# Test case
M = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

K = [
    [1, 0],
    [0, -1]
]

output = convolution_2d_numpy(M, K)
for row in output:
    print(row)



# Why is this solution better?
# Vectorized Operations:

# Instead of manually iterating over kernel elements, NumPy performs element-wise multiplication efficiently.
# matrix[i:i+k, j:j+k] * kernel applies broadcasting, which speeds up computations.
# Memory Efficiency:

# Since NumPy handles operations at the C-level, it reduces Python's loop overhead.
# Uses an optimized internal representation for numbers.
# Performance Gain:

# The new approach is significantly faster than the explicit nested loop version, especially for large matrices.


# Time Complexity O(MxN)
# Space Complexity best O((M-K+1) x (N-K+1))  worst  O(MxN)

def solution(a):
    n = len(a)  # Get the length of the input array
    r = [0] * n  # Initialize an array 'r' to store the count of groups with mean rank
                 # 'n' elements are initialized to 0
    
    # Outer loop to iterate over each index in the input array 'a'
    for i in range(n):
        s = 0  # Initialize the sum 's' to 0
        # Inner loop to iterate over the elements from index 'i' to the end of the array
        for j in range(i, n):
            s += a[j]  # Incrementally add each element to the sum 's'
            t = j - i + 1  # Calculate the length of the subarray
            # Check if the sum 's' divided by the length 't' is an integer
            if s % t == 0:
                r[s // t - 1] += 1  # Increment the count of groups with mean 's // t'
                                     # Adjusted by -1 because the mean starts from 1
    return r  # Return the array 'r' containing the count of groups with mean rank

print(solution([1, 2, 3, 4, 5]))  # Call the solution function with an example input

#To analyze the time complexity of the provided code, let's break it down:

#Outer loop iterates over each index i in the input array a. This loop runs n times.
#Inner loop iterates over elements starting from index i up to the end of the array a. In the worst case, when i is at the beginning of the array, this loop runs n times. However, as i progresses, the number of iterations decreases, but in the average case, it still contributes to a complexity proportional to n.
#Inside the inner loop, there are constant-time operations (addition, subtraction, modulo, division, and array access).
#Overall, the time complexity is dominated by the nested loops, resulting in O(n^2), where 'n' is the length of the input array a. Therefore, the time complexity of the provided code is O(n^2).

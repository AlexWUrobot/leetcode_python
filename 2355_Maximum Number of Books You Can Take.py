# https://algo.monster/liteproblems/2355
from typing import List
class Solution:
    def maximumBooks(self, books: List[int]) -> int:
        # Adjust the books count considering the position constraint
        adjusted_books = [count - idx for idx, count in enumerate(books)]
        n = len(adjusted_books)
      
        # Initialize the left limit for each book stack
        left_limits = [-1] * n
        stack = []
      
        # Compute left limits for each position based on the adjusted book counts
        for idx, value in enumerate(adjusted_books):
            while stack and adjusted_books[stack[-1]] >= value:
                stack.pop()
            if stack:
                left_limits[idx] = stack[-1]
            stack.append(idx)
      
        max_books = 0  # This will hold the maximum number of books that can be collected
        dp = [0] * n   # Dynamic programming array to store the best solution up to the current index
      
        # Initialize the first position
        dp[0] = books[0]
      
        # Calculate the maximum books for each position
        for i, book_count in enumerate(books):
            left_bound = left_limits[i]
            # Determine the number of books that can be collected at position i
            stack_height = min(book_count, i - left_bound)
          
            # Calculate the first book count
            first_book = book_count - stack_height + 1
          
            # Calculate the sum of the arithmetic series
            stack_books = (first_book + book_count) * stack_height // 2
          
            # If there is no left bound, do not add any previous book count, else add dp[left_bound]
            dp[i] = stack_books if left_bound == -1 else stack_books + dp[left_bound]
            # Update the maximum books if the current position has a better solution
            max_books = max(max_books, dp[i])
      
        # Return the maximum number of books that can be collected
        return max_books

# Example usage:
# sol = Solution()
# max_collectable_books = sol.maximumBooks([1, 3, 3, 2, 1])
# print(max_collectable_books)  # Output will vary depending on the input list `books`

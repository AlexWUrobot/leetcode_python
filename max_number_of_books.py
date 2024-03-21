# https://leetcode.com/discuss/interview-question/4291609/Amazon-or-SDE-Online-Assessment
def max_books(arr):
    book_counts = {}
    output = []
    
    for num in arr:
        print(num)
        if num > 0:
            # If the number is positive, increment the count of that book.
            book_counts[num] = book_counts.get(num, 0) + 1
        else:
            # If the number is negative, decrement the count of that book.
            book_counts[-num] = max(book_counts.get(-num, 0) - 1, 0)
        
        # Find the maximum count among the books at the current index.
        max_count = max(book_counts.values(), default=0)
        
        output.append(max_count)
        print(output)
    
    return output

# Example usage:
arr = [2, 3, 3, -3, 1]
print(max_books(arr))

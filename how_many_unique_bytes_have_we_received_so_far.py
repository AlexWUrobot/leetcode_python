# https://chatgpt.com/share/67f02364-114c-8005-b469-6cd2164d2a8b


# “How many unique bytes have we received so far?”
# def solution(segments):
    
#     received_bytes = set()
#     result = []
    
#     for segment in segments:
#         start, end = segment
        
#         received_bytes.update(range(start, end+1))
#         print("----", received_bytes)
#         result.append(len(received_bytes))

#     return result
#  Time Complexity: O(L) where L = total number of bytes processed (i.e., total length of all segments combined)
#  Space Complexity: O(R + n) received_bytes is a set of unique bytes seen so far → in worst case, it stores up to R unique elements, result stores n integers (one per segment)



# Tests passed: 12/20. Memory limit exceeded on test 13: Program exceeded the allowed memory limit. Optimize memory usage and try again.

# Keep a list of merged, non-overlapping intervals
def solution(segments):
    merged = []
    result = []

    def insert_interval(interval):
        nonlocal merged
        new_start, new_end = interval
        temp = []
        placed = False

        for s, e in merged:  # merged list 
            if e < new_start - 1:    # new interval, total after cur merge
                temp.append((s, e))
            elif new_end < s - 1:  # new interval, total before cur merge
                if not placed:
                    temp.append((new_start, new_end))
                    placed = True
                temp.append((s, e))
            else:                    # new interval overlapping
                new_start = min(new_start, s)
                new_end = max(new_end, e)
        if not placed:
            temp.append((new_start, new_end))
        merged = temp

    def count_total_length():
        return sum(e - s + 1 for s, e in merged)

    for segment in segments:
        insert_interval(tuple(segment))
        print("merge: ", merged)
        result.append(count_total_length())

    return result
    
    
# def solution(segments):
#     merged = []
#     result = []

#     def insert_interval(interval):
#         nonlocal merged   
#         new_start, new_end = interval
#         temp = []
#         placed = False

#         for s, e in merged: 
#             if e < new_start - 1:   
#                 temp.append((s, e))
#             elif new_end < s - 1: 
#                 temp.append((s, e))
#             else:                    
#                 new_start = min(new_start, s)
             
#         temp.append((new_start, new_end)) 
#         merged = temp

#     def count_total_length():
#         return sum(e - s + 1 for s, e in merged)

#     for segment in segments:
#         insert_interval(tuple(segment))
#         print("merge: ", merged)
#         result.append(count_total_length())

#     return result    
# https://chatgpt.com/share/67f02364-114c-8005-b469-6cd2164d2a8b
 # https://chatgpt.com/share/67f02364-114c-8005-b469-6cd2164d2a8b  
# Time: O(n * m)  # n segments, m intervals 
# space: O(n ) #  list of size n 
segments = [[1, 1], [2, 2], [3, 3]]    
print(solution(segments))  # [1, 2, 3]


segments = [[1, 1], [2, 2], [3, 5]]  
print(solution(segments))  # [1, 2, 5].

segments = [[1, 9], [1, 3], [8, 15], [6, 9], [2, 5]]
print(solution(segments))  # [9, 9, 15, 15, 15].


segments = [[7, 9], [1, 3], [8, 15], [6, 9], [2, 4]]
print(solution(segments))   # [3, 6, 12, 13, 14]

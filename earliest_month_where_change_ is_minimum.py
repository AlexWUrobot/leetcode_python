def find_earliest_month(arr):
    month = 0
    change = float('inf')
    tsum = 0
    s = 0
    n = len(arr)
    for i in range(n):
        tsum += arr[i]
    avg1 = 0
    avg2 = 0
    for i in range(n):
        s += arr[i]
        avg1 = s // (i + 1)
        avg2 = tsum // n
        if abs(avg1 - avg2) < change:
            change = abs(avg1 - avg2)
            month = i + 1
    return month

# Your code execution starts here
if __name__ == "__main__":
    arr = [1, 3, 2, 3]
    print(find_earliest_month(arr))

# https://leetcode.com/discuss/interview-question/1863401/find-the-earliest-month-where-change-is-minimum-in-java

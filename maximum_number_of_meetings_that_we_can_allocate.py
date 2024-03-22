
# https://leetcode.com/discuss/interview-question/1333699/Amazon-Online-Assessment-Problems-2021-July
def max_meetings(arrival, duration):
    # Create pairs of arrival and finish times
    meetings = sorted([(arrival[i], arrival[i] + duration[i]) for i in range(len(arrival))], key=lambda x: x[1])
    
    # Initialize the count of meetings and the end time of the last meeting
    count = 0
    end_time = 0
    
    # Iterate through the meetings
    for start, end in meetings:
        # If the start time is greater than or equal to the end time of the last meeting
        if start >= end_time:
            # Increment the count and update the end time
            count += 1
            end_time = end
    
    return count

# Example usage:
arrival_time = [1, 3, 5]
duration = [2, 2, 2]
print(max_meetings(arrival_time, duration))

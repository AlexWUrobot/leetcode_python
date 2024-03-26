# https://leetcode.com/discuss/interview-question/4709758/Amazon-OA-SDE2/

# Learn Haln's comments
# "
# The wording is a little weird, but maximum rush HAPPENED at 5 in tc1, and maximum rush HAPPENED at 4 to 8, and 10 to 20 in tc2.
# Maximum rush is the time period during which the maximum users from the given data are logged in. In other words, the amount of time where the number of concurrent users was at it's highest.

# So in tc1, at time 5, there were 3 users logged in. At no other time were there 3 users logged in, so the answer is 3 users x 1 time unit = 3.
# In tc2, there is only 1 user logged in at most at any given time. There was 1 user logged in from 4 to 8, and another user logged in from 10 to 20. So the answer is 1 user x (8-4+1) + 1 user x (20-10+1) which is 16. We add 1 because we are inclusive of login and logout times counting as active.
# "

# Write extra cases
# Given lots of intervals of login and logout of users, 
# write a python code to calculate to choose the highest number of same time users 
# and the overlap period.
# Case 1 :
# login: [1,5,5]
# logout: [5,10,5]
# output: 3, [5]
# the highest number of same time users  is 3
# the overlap  period is [5]. 

# Case 2:
# login: [1,3]
# logout: [5,10]
# output: 2, [3,4,5]
# the highest number of same time users  is 2
# the overlap  period is [3,4,5]. 

# Case  3:
# login: [4,10]
# logout: [5,12]
# output: 1, [4,5,10,11,12]
# the highest number of same time users  is 1
# the overlap  period is [4,5,10,11,12].

def find_max_overlap(login, logout):
    # Create a list of all login and logout times
    times = []
    for i in range(len(login)):
        times.append((login[i], 'login'))
        times.append((logout[i], 'logout'))

    # Sort the times by the hour, then by login before logout
    times.sort(key=lambda x: (x[0], x[1]))

    max_users = 0
    current_users = 0
    overlap = []
    for time in times:
        
        if time[1] == 'login':
            current_users += 1
            # If the current number of users is greater than max_users, update max_users and reset overlap
            if current_users > max_users:
                max_users = current_users
                overlap = [time[0]]
            # If the current number of users equals max_users, append the time to overlap
            elif current_users == max_users:
                overlap.append(time[0])
        else:
            # If the logout time is part of the overlap, add it to the list
            if current_users == max_users:
                overlap.append(time[0])
            current_users -= 1
        #print('time:',time,'current_users:',current_users,'max_users:',max_users,'overlap:',overlap) # since already sort, so it will only push to highest value

    # print('-----------overlap',overlap)
    # Convert overlap to a range of hours
    if len(overlap) <= 2:
        overlap_range = list(range(min(overlap), max(overlap)+1))
    else:
        index_array = list(range(0, len(overlap), 2))
        #print(index_array)
        overlap_range = []
        for i in index_array:
            temp = list(range(overlap[i], overlap[i+1]+1))
            overlap_range.extend(temp)
    
    
    rush_time_usage = max_users*len(overlap_range)
    return max_users, overlap_range,rush_time_usage

# Test cases
print(find_max_overlap([1,3,11], [5,10,12]))  # Case 1
print(find_max_overlap([1,5,5], [5,10,5]))  # Case 2
print(find_max_overlap([4,10], [8,20]))  # Case 3

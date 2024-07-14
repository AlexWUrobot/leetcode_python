
# https://www.fastprep.io/problems/amazon-group-students
def group_students(levels, max_spread):
    # Sort the levels in ascending order
    levels.sort()
    
    # Initialize the number of classes and the current level
    classes = 1
    cur_level = levels[0]
    
    # Iterate through each level
    for level in levels:
        # Check if the difference between the current level and cur_level exceeds max_spread
        if (level - cur_level) > max_spread:
            # Increment the number of classes and update cur_level
            classes += 1
            cur_level = level
    
    # Return the total number of classes
    return classes
    
levels = [1, 4, 7, 3, 4]
maxSpread = 2
print(group_students(levels, maxSpread))

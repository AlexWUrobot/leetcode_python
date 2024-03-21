# https://leetcode.com/discuss/interview-question/1688196/Amazon-or-Online-Assessment-or-Maximum-Number-of-Engineering-Teams
# similar : https://leetcode.com/problems/maximum-performance-of-a-team/description/

def max_eng(team_size, maxdiff, skill):
    i = 0  # Start index for the current team
    teams = 0  # Counter for the number of valid teams
    skill.sort()  # Sort the skills in ascending order

    # Iterate over the skill list
    while i < len(skill):
        # Check if there are enough engineers left to form a team
        if i + team_size - 1 >= len(skill):
            break  # Exit the loop if not enough engineers

        # Check if the current team satisfies the maxDiff constraint
        if skill[i+team_size-1] - skill[i] > maxdiff:
            i += 1  # Move to the next engineer if the constraint is not met
            continue  # Skip the rest of the loop and check the next team

        # If the team is valid, increment the team counter
        teams += 1
        # Move the index to the start of the next potential team
        i += team_size

    return teams  # Return the total number of valid teams formed

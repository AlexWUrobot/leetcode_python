# https://fastprep.gitbook.io/amazon-2024-oa/count-max-num-teams-or-ft
# https://www.fastprep.io/problems/count-max-num-teams
def countMaxNumTeams(skill, teamSize, maxDiff):
    skill.sort()  # Sort the skill levels
    teams = []  # List to store the formed teams
    n = len(skill)
    
    i = 0
    while i <= n - teamSize:
        # Check the difference between the maximum and minimum skill levels in the team
        if skill[i + teamSize - 1] - skill[i] <= maxDiff:
            teams.append(skill[i:i+teamSize])  # Append the team to the list of teams
            i += teamSize
        else:
            i += 1
            
    return len(teams), teams

# Example usage:
skill = [3, 4, 3, 1, 6, 5]
teamSize = 3
maxDiff = 2
num_teams, teams_list = countMaxNumTeams(skill, teamSize, maxDiff)
print("Number of teams:", num_teams)
print("Separate teams:")
for team in teams_list:
    print(team)

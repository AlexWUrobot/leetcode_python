#https://www.fastprep.io/problems/uber-find-top-two-teams

from typing import List

def findTopTwoTeams(wins: List[int], draws: List[int], scored: List[int], conceded: List[int]) -> List[int]:
    n = len(wins)
    teams = []
    
    for i in range(n):
        points = wins[i] * 3 + draws[i] * 1
        goal_difference = scored[i] - conceded[i]
        teams.append((points, goal_difference, i))
    
    # Sort teams based on points first, then goal difference, then index
    teams.sort(key=lambda x: (-x[0], -x[1], x[2]))
    
    return [teams[0][2], teams[1][2]]

# Example usage:
wins = [1, 2, 3]
draws = [1, 1, 1]
scored = [10, 20, 30]
conceded = [12, 23, 12]
print(findTopTwoTeams(wins, draws, scored, conceded))  # Output: [2, 1]

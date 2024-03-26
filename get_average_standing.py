# https://www.fastprep.io/problems/get-average-standing
# https://fastprep.gitbook.io/amazon-2024-oa/get-average-standing-or-ft

from fractions import Fraction

def getAverageStanding(d, records):
    # Initialize a dictionary to store race results
    race_results = {}
    for race_id, player_id, player_time in records:
        if race_id not in race_results:
            race_results[race_id] = []
        race_results[race_id].append((player_time, player_id))
    
    # Sort the race results based on time and player id
    for race_id in race_results:
        race_results[race_id].sort()
    
    # Calculate the standings for each player
    standings = {player_id: [] for player_id in range(d)}
    for race_id, results in race_results.items():
        for position, (player_time, player_id) in enumerate(results, start=1):
            standings[player_id].append(position)
    
    # Calculate the average standing for each player
    average_standings = []
    for player_id in range(d):
        if standings[player_id]:
            avg = Fraction(sum(standings[player_id]), len(standings[player_id])).limit_denominator()
            average_standings.append([avg.numerator, avg.denominator])
        else:
            average_standings.append([-1, -1])
    
    return average_standings

# Example usage:
d = 3
records = [[1, 1, 100], [1, 2, 200], [2, 1, 500]]
print(getAverageStanding(d, records))

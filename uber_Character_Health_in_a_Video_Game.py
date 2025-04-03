# https://www.fastprep.io/problems/uber-character-health-in-a-video-game
def final_health(initial_health, deltas):
    health = initial_health
    
    for delta in deltas:
        health += delta
        
        # Ensure health stays within [0, 100]
        if health < 0:
            health = 0
        elif health > 100:
            health = 100
    
    return health

# Example Usage
test_initial_health = 12
test_deltas = [-4, -12, 6, 2]
print(final_health(test_initial_health, test_deltas))  # Output: 8

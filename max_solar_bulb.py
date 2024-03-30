# https://www.fastprep.io/problems/amazon-maximize-solar-powered-bulbs

def maximizeSolarPoweredBulbs(bulbs):
    # Convert the string to a list for easier manipulation
    bulbs_list = list(bulbs)
    
    # Iterate over the bulbs, starting from the second bulb and ending at the second to last bulb
    for i in range(1, len(bulbs_list) - 1):
        # Check if the current bulb is electric-powered and not adjacent to solar-powered bulbs
        if bulbs_list[i] == '0' and bulbs_list[i-1] != '1' and bulbs_list[i+1] != '1':
            # Replace the electric-powered bulb with a solar-powered bulb
            bulbs_list[i] = '1'
    
    # Count the total number of solar-powered bulbs
    total_solar_bulbs = bulbs_list.count('1')
    
    return total_solar_bulbs

# Example usage:
bulbs = "1111110001"
print(maximizeSolarPoweredBulbs(bulbs))  # Output: 8

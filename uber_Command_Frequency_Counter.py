# https://www.fastprep.io/problems/uber-command-frequency-counter

def commandFrequencyCounter(commands):
    # Initialize frequency dictionary
    freq = {"cmd1": 0, "cmd2": 0, "cmd3": 0}
    
    # List to store actual commands as we process the input
    resolved_commands = []
    
    for cmd in commands:
        if cmd.startswith("!" ):  # It's a reference to a previous command
            index = int(cmd[1:]) - 1  # Convert to 0-based index
            if 0 <= index < len(resolved_commands):
                actual_cmd = resolved_commands[index]  # Retrieve original command
                freq[actual_cmd] += 1  # Update frequency
                resolved_commands.append(actual_cmd)  # Append to resolved list
        else:
            freq[cmd] += 1  # Update frequency
            resolved_commands.append(cmd)  # Append to resolved list
    
    return [freq["cmd1"], freq["cmd2"], freq["cmd3"]]

# Example usage
test_commands = ["cmd1", "cmd2", "cmd3", "!1", "!2", "cmd3", "cmd1"]
print(commandFrequencyCounter(test_commands))  # Output: [3, 2, 2]

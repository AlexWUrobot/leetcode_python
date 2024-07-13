# https://www.fastprep.io/problems/amazon-get-max-consecutive-on


def getMaxConsecutiveON(server_states: str, k: int) -> (int, str):
    n = len(server_states)
    max_on_servers = 0
    best_states = server_states
    
    # If k is 0, find the maximum consecutive 'ON' servers without any flips
    if k == 0:
        current_max = 0
        current_count = 0
        for state in server_states:
            if state == '1':
                current_count += 1
                current_max = max(current_max, current_count)
            else:
                current_count = 0
        
        return current_max, server_states
    
    # Otherwise, proceed with the original logic to find the maximum using flips
    
    for operations in range(k):
        if operations > 0:
                server_states = list(second_operation_best)        
        for i in range(n):
            for j in range(i, n):
                temp_server_states = list(server_states)

                     
                stop_count = False    
                # Flip the segment from i to j
                for m in range(i, j + 1):
                    if temp_server_states[m] == '0':
                        temp_server_states[m] = '1'
                    else:
                        stop_count = True
                        break   # if touch the 1, than stop 
                        #temp_server_states[m] = '0'
                if stop_count == True:
                    break

                
                print("operations", operations,"temp_server_states:",temp_server_states)

                # Count the maximum number of consecutive '1's
                current_max = 0
                current_count = 0
                
                
                
                for idx, state in enumerate(temp_server_states):
                    if state == '1':
                        current_count += 1
                        current_max = max(current_max, current_count)
                    else:
                        current_count = 0
                
                if current_max > max_on_servers: # save the best 
                    max_on_servers = current_max
                    best_states = temp_server_states
        
        second_operation_best = best_states
        print("operations:==========",operations, second_operation_best)            
 
        
        
    return max_on_servers, best_states

# Example :
server_states1 = "00100010"
k1 = 2
max_on1, states1 = getMaxConsecutiveON(server_states1, k1)
print(f"Max consecutive 'ON' servers: {max_on1}")
print(f"Modified server states: {states1}")  # Output: "1"

server_states2 = "1001"
k2 = 1
max_on2, states2 = getMaxConsecutiveON(server_states2, k2)
print(f"Max consecutive 'ON' servers: {max_on2}")
print(f"Modified server states: {states2}")  # Output: "2"

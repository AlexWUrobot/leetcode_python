# https://www.fastprep.io/problems/amazon-process-queue


def remove_elements(lst, k):
    return [x for x in lst if x != k]
    
def process_queue(wait):
    
    n = len(wait)
    wait_process = []
    t = 0
    while wait != []:
        # remove one elemnt 
        wait = wait[1:]
        wait = remove_elements(wait, t)
        wait_process.append(len(wait))
        t = t + 1
    return wait_process

# Example usage:
wait = [2, 2, 3, 1]
output = process_queue(wait)
print(output)  # Output: [3, 1, 0]

# Example usage:
wait =  [4,3,1,2,1]
output = process_queue(wait)
print(output)  # Output: [4,1,0] 

wait = [3,4,4,4]
output = process_queue(wait)
print(output) # [3,2,1,0] 

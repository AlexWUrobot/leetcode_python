#https://www.fastprep.io/problems/amazon-count-number-of-retailers

def count_number_of_retailers(retailers, requests):
    n = len(requests)
    m = len(retailers)
    ans = [0] * n
    
    def check_inside_rectangle(a, b, left, bottom, right, top):
        return left <= a <= right and bottom <= b <= top
    
    for j in range(n):
        a, b = requests[j]
        cnt = 0
        
        for i in range(m):
            x, y = retailers[i]
            
            # Calculate the rectangle coordinates for the ith retailer
            rect_left = min(0, x)
            rect_right = max(0, x)
            rect_bottom = min(0, y)
            rect_top = max(0, y)
            
            if check_inside_rectangle(a, b, rect_left, rect_bottom, rect_right, rect_top):
                cnt += 1
        
        ans[j] = cnt
    
    return ans
    


retailers = [[1, 2], [2, 3], [1, 5]]
requests = [[1, 1], [1, 4]]
print(count_number_of_retailers(retailers, requests))

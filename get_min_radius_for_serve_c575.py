# https://yuihuang.com/zj-c575/
# https://zerojudge.tw/ShowProblem?problemid=c575
def get_min_radius(k,lst):
        # k is how many server
    n = len(lst) # the total number of the location who need the service  
    lst.sort()
         
    dis = lst[-1] - lst[0]
    if dis <= 2:
        return(1)
        #print(1)
        #continue
 
    mn = 1                  # search range minum 
    mx = int(dis/k) + 1     # search range maximum 
 
    while True:
        mid = (mn + mx) // 2
        count = 0
        start = 0
        for j in range(k):
            dis2 = lst[start] + mid
            count += 1
            for l in range(start, n):
                if lst[l] > dis2:
                    start = l
                    break
            else:
                mx = mid
                break
        else:
            mn = mid + 1
 
        if mn == mx:
            #print(mn)
            return(mn)
            break
    

lst = [5, 1, 2, 8, 7]
k = 2
ans = get_min_radius(k,lst)
print(ans)  # 3


lst = [7, 5, 1, 2, 8]
k = 1
ans = get_min_radius(k,lst)
print(ans)  # 7
        

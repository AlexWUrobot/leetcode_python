# https://www.fastprep.io/problems/amazon-ordered-configuration

def getExperience(xp):
    xp.sort()
    i, j = 0, len(xp) - 1
    dp = set()
    while i < j:
        avg = (xp[i] + xp[j]) / 2
        dp.add(avg)  # adding set, will not repeat the number
        i += 1
        j -= 1
        # print("dp:",dp)

    return len(dp)
    
    
xp = [1, 4, 1, 3, 5, 6]
print(getExperience(xp))  # 2 


xp = [1, 1, 1, 1, 1, 1]
print(getExperience(xp))  # 1


xp = [1, 100, 10, 1000]
print(getExperience(xp))  # 2
# Time complexity O(n log n)


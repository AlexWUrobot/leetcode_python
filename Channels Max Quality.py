# https://www.fastprep.io/problems/amazon-calculate-median-sum

def findMedian(i, j, packets):
    if (i + j) % 2 != 0:
        ind = (i + j) // 2
        result = (packets[ind] + packets[ind + 1]) / 2.0
        return result
    return packets[(i + j) // 2]

def findMaximumQualityfunc(packets, channels, i, j):
    if channels < 0:
        return float('-inf')  # Equivalent to Double.MIN_VALUE in Java
    if j == len(packets) - 1:
        if channels == 0:
            return findMedian(i, j, packets)
        else:
            return float('-inf')
    ans1 = findMaximumQualityfunc(packets, channels, i, j + 1)
    ans2 = findMedian(i, j, packets) + findMaximumQualityfunc(packets, channels - 1, j + 1, j + 1)
    return max(ans1, ans2)

def findMaximumQuality(packets, channels):
    packets.sort()
    return round(findMaximumQualityfunc(packets, channels - 1, 0, 0))

packets = [1, 2, 3, 4, 5]
channels = 2
print(findMaximumQuality(packets, channels)) # 8 


packets = [5, 2, 2, 1, 5, 3]
channels = 2
print(findMaximumQuality(packets, channels)) # 7

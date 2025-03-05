# https://www.fastprep.io/problems/amazon-minimize-maximum-parcels

def minimizeMaximumParcels(parcels, extraParcels):
  left, right = min(parcels), max(parcels) + extraParcels
  res = -1

  def isPossible(lim):
    parcelsLeft = extraParcels
    for i in range(len(parcels)):
      parcelsLeft -= (lim - parcels[i])
      if parcelsLeft <= 0:
        break

    return True if parcelsLeft <= 0 else False

  while left <= right:
    mid = left + (right - left) // 2
    if isPossible(mid):
      res = mid
      right = mid - 1
    else:
      left = mid + 1

  return res

# Example test cases
packages = [7, 5, 1, 9, 1]
extra_packages = 25
print("Output:", minimizeMaximumParcels(packages, extra_packages))  # Output: 10 
packages = [1, 2, 3]
extra_packages = 3
print("Output:", minimizeMaximumParcels(packages, extra_packages)) #  Output: 3
packages = [1]
extra_packages = 3
print("Output:", minimizeMaximumParcels(packages, extra_packages)) #  Output: 4 

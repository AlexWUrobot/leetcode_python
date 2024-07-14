# https://www.fastprep.io/problems/get-max-points-from-sprints

def get_maximum_points(days, k):
    total_days = sum(days)

    # Check if k is larger than the total days counted
    if k > total_days:
        k = total_days

    # Create points array
    points = []
    for sprint in days:
        points.extend(range(1, sprint + 1))

    # Calculate initial points for the first k days
    max_points = 0
    current_points = sum(points[:k])
    max_points = current_points

    # Slide the window
    for i in range(1, total_days):
        current_points -= points[(i - 1) % total_days]
        if i + k - 1 < total_days:
            current_points += points[i + k - 1]
        else:
            current_points += points[(i + k - 1) % total_days]
        max_points = max(max_points, current_points)

    return max_points

days = [2, 3, 2]
k = 4
print(get_maximum_points(days, k))

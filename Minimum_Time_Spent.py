# https://fastprep.gitbook.io/amazon-2024-oa/minimum-time-spent-or-ft
# https://www.fastprep.io/problems/minimum-time-spent

def minimumTimeSpent(comedyReleaseTime, comedyDuration, dramaReleaseTime, dramaDuration):
    # Sort the movies by their finish time (release time + duration)
    comedy_movies = sorted(zip(comedyReleaseTime, comedyDuration), key=lambda x: x[0] + x[1])
    drama_movies = sorted(zip(dramaReleaseTime, dramaDuration), key=lambda x: x[0] + x[1])

    # Initialize the earliest finish time to infinity
    earliest_finish_time = float('inf')

    # Check every combination of comedy and drama movies
    for c_release, c_duration in comedy_movies:
        for d_release, d_duration in drama_movies:
            # Calculate the finish time if we watch the comedy first, then the drama
            finish_time = max(c_release + c_duration, d_release) + d_duration
            # Update the earliest finish time
            earliest_finish_time = min(earliest_finish_time, finish_time)

            # Calculate the finish time if we watch the drama first, then the comedy
            finish_time = max(d_release + d_duration, c_release) + c_duration
            # Update the earliest finish time
            earliest_finish_time = min(earliest_finish_time, finish_time)

    return earliest_finish_time

# Example usage:
comedyReleaseTime = [1, 4]
comedyDuration = [3, 2]
dramaReleaseTime = [5, 2]
dramaDuration = [2, 2]
print(minimumTimeSpent(comedyReleaseTime, comedyDuration, dramaReleaseTime, dramaDuration))

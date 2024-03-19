# https://leetcode.com/discuss/interview-question/4834742/amazon-online-assessment
def earliest_finish_time(comedyReleaseTime, comedyDuration, dramaReleaseTime, dramaDuration):
    # Pair each movie's release time with its duration and sort
    comedyMovies = sorted(zip(comedyReleaseTime, comedyDuration), key=lambda x: x[0])
    dramaMovies = sorted(zip(dramaReleaseTime, dramaDuration), key=lambda x: x[0])
    
    # Initialize pointers for each category
    comedyPointer, dramaPointer = 0, 0
    earliestTime = 0
    
    # Loop until you have watched one movie from each category
    while comedyPointer < len(comedyMovies) and dramaPointer < len(dramaMovies):
        comedyEnd = comedyMovies[comedyPointer][0] + comedyMovies[comedyPointer][1]
        dramaEnd = dramaMovies[dramaPointer][0] + dramaMovies[dramaPointer][1]
        
        # Select the movie that ends earlier
        if comedyEnd <= dramaEnd:
            earliestTime = max(earliestTime, comedyEnd)
            comedyPointer += 1
        else:
            earliestTime = max(earliestTime, dramaEnd)
            dramaPointer += 1
        
        # If one movie from each category has been watched, break
        if comedyPointer > 0 and dramaPointer > 0:
            break
    
    return earliestTime

# Example usage:
comedyReleaseTime = [1, 4]
comedyDuration = [3, 2]
dramaReleaseTime = [5, 2]
dramaDuration = [2, 2]

print(earliest_finish_time(comedyReleaseTime, comedyDuration, dramaReleaseTime, dramaDuration))

# https://www.fastprep.io/problems/find-minimum-pages-per-day

def min_pages_per_day(pages, days):
    total_pages = sum(pages)
    if total_pages <= days:
        return max(pages)
    
    low, high = 1, max(pages)
    while low < high:
        mid = (low + high) // 2
        days_needed = 0
        for page_count in pages:
            days_needed += (page_count + mid - 1) // mid
        
        if days_needed > days:
            low = mid + 1
        else:
            high = mid
    
    days_needed = 0
    for page_count in pages:
        days_needed += (page_count + low - 1) // low
    
    if days_needed <= days:
        return low
    else:
        return -1

# Example usage:
pages = [5, 3, 1]
days = 4
print(min_pages_per_day(pages, days))  # Output: 4

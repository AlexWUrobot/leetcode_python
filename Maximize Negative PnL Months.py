# https://www.fastprep.io/problems/amazon-maximize-negative-pnl_months
def maximize_negative_pnl_months(PnL):
    def recursive_helper(index, cumulative_sum, negative_months):
        # Base case: if all months are processed, return the count of negative months
        if index == len(PnL):
            return negative_months

        # Option 1: Leave the PnL as is and move to the next month
        max_negative_months = recursive_helper(index + 1, cumulative_sum + PnL[index], negative_months)

        # Option 2: Flip the sign of the PnL for the current month if it does not make the cumulative sum non-positive
        if cumulative_sum - PnL[index] > 0:
            max_negative_months = max(max_negative_months, 
                                      recursive_helper(index + 1, cumulative_sum - PnL[index], negative_months + 1))

        return max_negative_months

    # Start the recursion from index 0 with initial cumulative sum and zero negative months
    return recursive_helper(0, 0, 0)
    
PnL = [5, 3, 1, 2]
ans = maximize_negative_pnl_months(PnL)
print("PnL",PnL, "ans: ",ans)

PnL = [1, 1, 1, 1, 1]
ans = maximize_negative_pnl_months(PnL)
print("PnL",PnL, "ans: ",ans)

PnL = [5, 2, 3, 5, 2, 3]
ans = maximize_negative_pnl_months(PnL)
print("PnL",PnL, "ans: ",ans)

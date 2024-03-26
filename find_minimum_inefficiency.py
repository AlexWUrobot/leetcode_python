# https://www.fastprep.io/problems/find-minimum-inefficiency
# https://fastprep.gitbook.io/amazon-2024-oa/2023-june-aug/find-minimum-inefficiency
def findMinimumInefficiency(serverType):
    # Helper function to calculate inefficiency
    def calculateInefficiency(s):
        return sum(s[i] != s[i+1] for i in range(len(s) - 1))

    # Replace '?' with '0' or '1' and calculate inefficiencies
    def replaceAndCalculate(s, index):
        if index == len(s):
            return calculateInefficiency(s)
        if s[index] == '?':
            # Try both '0' and '1' for each '?'
            return min(replaceAndCalculate(s[:index] + '0' + s[index+1:], index+1),
                       replaceAndCalculate(s[:index] + '1' + s[index+1:], index+1))
        else:
            return replaceAndCalculate(s, index+1)

    # Start the recursive replacement and calculation from the first index
    return replaceAndCalculate(serverType, 0)

# Example usage:
serverType1 = "??011??0"
print(findMinimumInefficiency(serverType1))  # Output: 2

serverType2 = "00?10??1?"
print(findMinimumInefficiency(serverType2))  # Output: 3

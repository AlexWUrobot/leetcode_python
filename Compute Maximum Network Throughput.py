# https://www.fastprep.io/problems/1.amazon-get-max-throughput
# https://chatgpt.com/share/67c77f1f-ec1c-8005-adf4-e40c52b71cb2

def amazonGetMaxThroughput( host_throughput):
    ans = 0
    host_throughput.sort()
    lf,rt = 0, len(host_throughput)-1
    while rt - lf >= 2:
      ans += host_throughput[rt-1]
      rt -= 2
      lf += 1
    return ans
        
        
# Example usage
serverRates = [4, 6, 3, 5, 4, 5]
print(amazonGetMaxThroughput(serverRates))

serverRates = [2, 3, 4, 3, 4]
print(amazonGetMaxThroughput(serverRates))

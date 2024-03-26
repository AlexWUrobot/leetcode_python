# https://leetcode.com/discuss/interview-question/1759477/amazon-new-grad-oa-2022-find-lowest-price
# https://leetcode.com/discuss/interview-question/1528869/amazon-oa-ng-2021

import collections

class Solution:
    def calculateDiscountedPrice(self, map, saleName, price, lowestPrice):
        if saleName == 'EMPTY' or saleName == None:
            return lowestPrice

        saleLevel, saleAmount = map[saleName]
        
        if saleLevel == 1:
            lowestPrice = min(lowestPrice, (price - price * saleAmount/100))
        if saleLevel == 2:
            lowestPrice = min(lowestPrice, (price - saleAmount))
        return lowestPrice

    def calculate_price(self, products, discounts):
        res = 0
        map = collections.defaultdict(list) # saleName: (saleLevel, saleAmount)
        
        for d in discounts:
            map[d[0]] = (int(d[1]), int(d[2]))
        print("map:", map)
        
        for p in products:
            price = int(p[0])
            lowestPrice = price
            
            for s in range(1, len(p)):
                lowestPrice = min(lowestPrice, self.calculateDiscountedPrice(map, p[s], price, lowestPrice))
            res += lowestPrice
        
        return res


if __name__ == '__main__':
    products=[['10','d0','d1'],['15','EMPTY','EMPTY'],['20','d1','EMPTY']]
    discounts=[['d0','1','27'],['d1','2','5']]
    # create a object
    s = Solution()
    #calling function
    print(s.calculate_price(products, discounts))

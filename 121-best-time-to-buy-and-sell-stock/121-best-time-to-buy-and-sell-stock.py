class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxSeen = -1
        minSeen = 100001
        maxProfit = 0
                
        for price in prices:
            if price < minSeen:
                minSeen = price
                maxSeen = -1
            elif price > maxSeen:
                maxSeen = price
            maxProfit = max(maxSeen - minSeen, maxProfit)
        
        return maxProfit
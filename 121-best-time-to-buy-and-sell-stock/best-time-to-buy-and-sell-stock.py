class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxpurchase = prices[0]
        maxprofit = 0
    
        for i in range(len(prices)):
            if prices[i] < maxpurchase:
                maxpurchase = prices[i]
                
            if prices[i] - maxpurchase > maxprofit:
                maxprofit = prices[i] - maxpurchase
        return maxprofit
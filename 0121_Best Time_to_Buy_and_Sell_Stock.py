class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = 999999
        maxPro = 0
        for i in range(len(prices)):
            minPrice = min(minPrice, prices[i])
            maxPro = max(maxPro, prices[i]-minPrice)
        return maxPro

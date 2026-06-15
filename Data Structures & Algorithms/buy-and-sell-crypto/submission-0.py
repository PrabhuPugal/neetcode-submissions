class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprice = float('inf')
        maxprof = 0

        for i in prices:
            minprice = min(minprice, i)
            maxprof = max(maxprof, i - minprice)

        return maxprof
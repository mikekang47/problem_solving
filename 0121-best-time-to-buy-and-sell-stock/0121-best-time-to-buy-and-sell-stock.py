class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m = 0
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                if prices[j] - prices[i] <= 0:
                    break
                else:
                    m = max(m, prices[j] - prices[i])
        return m
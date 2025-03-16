from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Track profit
        profit = 0
        # If price of i + 1 day is greater than i then buy i and sell at i + 1
        # realizing profit immediately
        # Number of transactions doesn't matter so can take advantage of that
        # for simpler code
        # end iteration 1 short of end since have essentially 2 pointers
        for i in range(len(prices) - 1):
            if prices[i + 1] > prices[i]:
                profit += prices[i + 1] - prices[i]

        return profit


solution = Solution()
print(solution.maxProfit([7, 1, 5, 3, 6, 4]))

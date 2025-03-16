from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Prices
        buy_price = prices[0]
        # Track transactions
        transactions = 0
        # Track profit
        total_profit = 0
        cur_profit = 0
        # Want to realize profit once the profit of the next day would be less
        for i in range(len(prices) - 1):
            if prices[i + 1] > prices[i]:
                if prices[i] < buy_price:
                    buy_price = prices[i]
                cur_profit = prices[i + 1] - buy_price
                continue
            if cur_profit > 0:
                total_profit += cur_profit
                cur_profit = 0
                transactions += 1
                buy_price = prices[i + 1]
        if cur_profit > 0:
            total_profit += cur_profit
            transactions += 1
        print('number of transactions:', transactions)
        return total_profit

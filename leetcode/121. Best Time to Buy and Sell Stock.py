from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0

        lowest_until_day_i_included = []
        lowest = prices[0]

        for day, p in enumerate(prices):
            if p < lowest:
                lowest = p
            lowest_until_day_i_included.append(lowest)

        max_profit = 0

        for day, p in enumerate(prices):
            # profit selling now, having bought at the lowest price until today.
            profit = p - lowest_until_day_i_included[day]

            if profit > max_profit:
                max_profit = profit

        return max_profit
        
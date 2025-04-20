from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        # profit after first buy, start at -inf because we want this to be -price at the first iteration.
        first_buy = float('-inf')

        # profit after first sell, start at 0 because it is the best profit before selling.
        first_sell = 0

        # Same logic as first_buy.
        second_buy = float('-inf')

        # Same logic as first sell.
        second_sell = 0
        
        for price in prices:
            first_buy = max(first_buy, -price)
            first_sell = max(first_sell, first_buy + price)
            second_buy = max(second_buy, first_sell - price)
            second_sell = max(second_sell, second_buy + price)
        
        return second_sell
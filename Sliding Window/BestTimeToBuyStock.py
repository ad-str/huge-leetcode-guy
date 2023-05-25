from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''My first attempt solution'''
        minprice = float("infinity")
        res = 0
        for price in prices:
            minprice = min(price, minprice)
            res = max(res, price - minprice)
        return res

    def maxProfit(self, prices: List[int]) -> int:
        '''Solution I found does not use float("infinity") but rather just the first element'''
        res = 0
        
        lowest = prices[0]
        for price in prices:
            if price < lowest:
                lowest = price
            res = max(res, price - lowest)
        return res

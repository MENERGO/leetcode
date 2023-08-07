class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        res = max(prices) - min(prices)
        mx = -1
        was = []
        for n, i in enumerate(prices):
            if i > prices[n - 1] and n > 0:
                continue
            if mx == res:
                break
            if i not in was:
                x = max(prices[n:]) - i
                if x > mx:
                    mx = x
                was.append(i)
        return mx


'''
        min_price = float('inf')
        max_profit = float('-inf')

        for p in prices:
            min_price = min(min_price, p)
            max_profit = max(max_profit, p - min_price)
            
        return max_profit
'''

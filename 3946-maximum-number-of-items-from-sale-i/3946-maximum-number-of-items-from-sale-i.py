class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        factors, prices = zip(*items)
        cheapest = min(prices)
        best = [money // cheapest for money in range(budget + 1)]  
        for factor, price in items:
            gain = sum(other % factor == 0 for other in factors) 
            for money in range(budget, price - 1, -1):  
                best[money] = max(best[money], best[money - price] + gain)
        return best[budget]
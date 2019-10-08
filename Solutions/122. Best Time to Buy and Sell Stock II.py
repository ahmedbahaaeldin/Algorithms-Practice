class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mapping = {day:value for day,value in enumerate(prices)}
        buyed = False
        buying_price = 0
        selling_price = 0
        profit = 0
        for days in mapping.keys():
            if days+1 == len(prices) and buyed == False:
                return profit
            elif days+1 == len(prices) and buyed == True:
                profit += mapping[days] - buying_price
                return profit
            if mapping[days] > mapping[days+1] and buyed == False:
                continue
            elif mapping[days] < mapping[days+1] and buyed == False:
                buyed = True
                buying_price = mapping[days]
            
            if mapping[days] > mapping[days+1] and buyed == True:
                selling_price = mapping[days]
                profit += selling_price - buying_price
                buyed = False
            elif days+1 !=len(prices) and mapping[days] < mapping[days+1] and buyed == True:
                continue
            
        
        return 0

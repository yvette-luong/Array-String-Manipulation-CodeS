'''
You are given the prices of a stock,
in the form of an array of integers, prices. 
Let's say that prices[i] is the price of the stock on the 'i^th' day (0-based index). 
Assuming that you are allowed to buy and sell the stock only once, your task is to find the maximum possible profit (the difference between the buy and sell prices).
Note: You can assume there are no fees associated with buying or selling the stock.

--Example
For prices = [6, 3, 1, 2, 5, 4], the output should be buyAndSellStock(prices) = 4.
It would be most profitable to buy the stock on day 2 and sell it on day 4. Thus, the maximum profit is prices[4] - prices[2] = 5 - 1 = 4.

For prices = [8, 5, 3, 1], the output should be buyAndSellStock(prices) = 0.
Since the value of the stock drops each day, there's no way to make a profit from selling it. Hence, the maximum profit is 0.

For prices = [3, 100, 1, 97], the output should be buyAndSellStock(prices) = 97.
It would be most profitable to buy the stock on day 0 and sell it on day 1. Thus, the maximum profit is prices[1] - prices[0] = 100 - 3 = 97.

--Input/Output
[execution time limit] 4 seconds (py3)

[input] array.integer prices

Guaranteed constraints:
1 ≤ prices.length ≤ 105,
1 ≤ prices[i] ≤ 106.

[output] integer

The maximum possible profit.

--Plan :
    Buy : loop through the lowest price in the array 
    Sell: loop through the highest price in the array 
    buy < sell 
    return : the highest num of profit 
'''
# py 
'''
this code block only passed 3 tests
'''
# def buyAndSellStock(prices):
#     profit = 0
#     buy = prices[0]
#     sell = 0
#     i = 1
#     while i < len(prices):
#         sell = prices[i]
#         if sell - buy > profit:
#             profit = sell - buy
#         if sell < buy:
#             buy = sell
#         i += 1
#     return profit 

def buyAndSellStock(prices):
    profit = 0
    buyingprice = prices[0]
    sellingprice = 0
    x = 1
    while x < len(prices):
        sellingprice = prices[x]
        if sellingprice - buyingprice > profit:
            profit = sellingprice - buyingprice
        if sellingprice < buyingprice:
            buyingprice = sellingprice
        x += 1
    return profit

# js

# Consider the sequence A = [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]. The maximum profit that can be made with one buy
# and one sell is 30 - buy at 260 and sell at 290.

# Write a program that takes an array denoting the daily stock price, and returns the maximum profit that could be made by 
# buying and selling one share of that stock.

def buy_and_sell_stock_once(prices):
    
    min_price_so_far = float('inf')
    max_profit = 0.0
    
    for price in prices:
        max_profit_sell_today = price - min_price_so_far
        max_profit = max(max_profit_sell_today, max_profit)
        min_price_so_far = min(price, min_price_so_far)
    return max_profit

A = [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]
buy_and_sell_stock_once(A)

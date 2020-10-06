
def maxProfitOneTransaction(prices):

    #max_profit = float('-inf')
    buy = prices[0]

    dp = [0] * len(prices)

    for i in range(1, len(prices)):
        buy = min(buy, prices[i])
        # max_profit = max(max_profit, prices[i] - buy)
        dp[i] = max(dp[i-1], prices[i] - buy)

    return dp[len(prices) - 1]

def maxProfitMultiTransaction(prices):

    max_profit = 0
    buy = prices[0]

    #dp = [0] * len(prices)

    for i in range(1, len(prices)):
        buy = min(buy, prices[i])
        if prices[i] > buy:
            #dp[i] = prices[i] - buy
            max_profit += prices[i] - buy #dp[i]
            buy = prices[i]

    return max_profit




# Say you have an array for which the ith element is the price of a given stock on day i.
# If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.
# Note that you cannot sell a stock before you buy one.

p = [7,1,5,3,6,4]
print(maxProfitOneTransaction(p))
print(maxProfitMultiTransaction([1,2,3,4,5]))
    
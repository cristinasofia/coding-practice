
# 622 https://leetcode.com/problems/coin-change/
def minNumberCoins(coins, amount):

    dp = [[float('inf') for _ in range(amount+1)] for _ in range(len(coins))]

    for i in range(len(coins)):
        for j in range(amount+1):
            if j == 0:
                dp[i][j] = 0
            elif j < coins[i]:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = min(dp[i-1][j], dp[i][j-coins[i]] + 1)
    
    return dp[len(coins)-1][amount]

# 518 https://leetcode.com/problems/coin-change-2/
def coinCombinations(coins, amount):

    dp = [[0 for _ in range(amount+1)] for _ in range(len(coins))]

    for i in range(len(coins)):
        for j in range(amount+1):
            if j == 0:
                dp[i][j] = 1
            elif j < coins[i]:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j - coins[i]]
    
    return dp[len(coins)-1][amount]


# Make sure coins are sorted ascending

"""
MINIMUM NUMBER OF COINS:
You are given coins of different denominations and a total amount of money amount. 
Write a function to compute the fewest number of coins that you need to make up that amount. 
If that amount of money cannot be made up by any combination of the coins, return -1.

EXPLANATION:

if j == 0: base case, no coins makes up 0 amount

    0   1   2   3   4   5   6   7   8   9   10  11
1   0   
2   0
5   0

if j < coins: copy above cell, since the minimum to make 1 cannot be made with coin[i] == 2

    0   1   2   3   4   5   6   7   8   9   10  11
1   0   1   2   3   4   5   6   7   8   9   10  11  
2   0   1
5   0

else: minimum of    (a) no. of coins needed to make 3 with prior coin 1 -> dp[i-1][j]
                    (b) no.of coins needed to make 3-2 = 1 -> dp[i][j-coin[i]]
                        then add 1

    0   1   2   3   4   5   6   7   8   9   10  11
1   0   1   2  (3)  4   5   6   7   8   9   10  11   
2   0  (1)  1  (2)
5   0

result:
    0   1   2   3   4   5   6   7   8   9   10  11
1   0   1   2   3   4   5   6   7   8   9   10  11
2   0   1   1   2   2   3   3   4   4   5   5   6  
5   0   1   1   2   2   1   2   2   3   3   2   3
"""

amount = 11
coins = [1, 2, 5]
# 3

print(minNumberCoins(coins, amount))

"""
NUMBER OF COMBINATIONS OF COINS:
You are given coins of different denominations and a total amount of money. 
Write a function to compute the number of combinations that make up that amount. 
You may assume that you have infinite number of each kind of coin.

EXPLANATION:

if j == 1: base case, only 1 way to make 0 amount

    0   1   2   3   4   5
1   1
2   1
5   1

elif j < coins[i]: copy above cell, since no. of ways to make amount is with lower denomination

    0   1   2   3   4   5
1   1   1   1   1   1   1
2   1   1
5   1

else: no. of ways to make coin is with no. of ways of previous coin at current amount, 
and no. of ways with current coin at amount - coin[i]

    0   1   2   3   4   5
1   1   1   1  (1)  1   1
2   1  (1)  2  (2)   
5   1    

result:

    0   1   2   3   4   5
1   1   1   1   1   1   1
2   1   1   2   2   3   3 
5   1   1   2   2   3   4
"""

amount = 5
coins = [1, 2, 5]
# 4

print(coinCombinations(coins, amount))
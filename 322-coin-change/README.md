<h2><a href="https://leetcode.com/problems/coin-change">Coin Change</a></h2> <img src='https://img.shields.io/badge/Difficulty-Medium-orange' alt='Difficulty: Medium' />

## approach:
- make an array dp of size amount + 1 and fill it with a large number (like infinity)
- set dp[0] = 0 because zero coins are needed to make amount 0
- for each value from 1 to amount, check all coins one by one
- if the coin can be used (i.e. x - coin >= 0), update dp[x] = min(dp[x], dp[x - coin] + 1)
- this means: to make amount x, try using coin c and add one coin to the best way of making x - c
- after filling the array, the answer is dp[amount] if it is not infinity, otherwise return -1

- Time complexity: O(amount * n)
- Space complexity: O(n)

 

<h2><a href="https://leetcode.com/problems/best-time-to-buy-and-sell-stock">Best Time to Buy and Sell Stock</a></h2> <img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' />

## approach:


- initialized minpurchase to first element in array, initialized maxprofit to 0
- iterated through array using for loop
     - if the price at current day is less than minpurchase, assign minpurchase equal current price
     - if difference of current price and minpurchase is greater than maxprofit, update maxprofit with that value
- return maxprofit

- Time complexity: O(n)
- Space complexity: O(1)

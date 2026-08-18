<h2><a href="https://leetcode.com/problems/house-robber-ii">House Robber II</a></h2> <img src='https://img.shields.io/badge/Difficulty-Medium-orange' alt='Difficulty: Medium' />

## approach:

- if length of nums array is 1, return that number as there exists no circle problem
- else, case1 - calculate with house 1 till the second last house to avoid circle problem
- case2 - calculate excluding house 1 till the last house to avoid circle problem
- return which case has more money to be robbed
- in rob_linear helper function, check if theres only 1 house, if yes return it
- create array dp of same length of given array nums, with all elements initialized with 0
- initialize 0th element with the corresponding number at array nums
- initialize 1st element with max of 0th and 1st element
- run for loop from 2nd element to end
- for each current house:
     - either skip current house i.e. dp[i - 1]
     - else rob current house i.e. num[i] + dp[i - 2]
     - store maximum of these 2 choices in dp[i]
- return d[n - 1]

- Time complexity: O(n)
- Space complexity: O(n) 

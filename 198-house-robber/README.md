<h2><a href="https://leetcode.com/problems/house-robber">House Robber</a></h2> <img src='https://img.shields.io/badge/Difficulty-Medium-orange' alt='Difficulty: Medium' />

## Approach:
- dp[i] = maximum money that can be robbed from houses 0 to i
- initialize:
- dp[0] = nums[0]
- dp[1] = max(nums[0], nums[1])
- for every next house, there are 2 choices:
- skip current house , dp[i-1]
- rob current house , nums[i] + dp[i-2]
- take the maximum of these two:
- dp[i] = max(dp[i-1], nums[i] + dp[i-2])
- return dp[n-1]

- Time Complexity: O(n)
- Space Complexity: O(n)

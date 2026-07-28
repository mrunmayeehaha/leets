<h2><a href="https://leetcode.com/problems/split-array-largest-sum">Split Array Largest Sum</a></h2> <img src='https://img.shields.io/badge/Difficulty-Hard-red' alt='Difficulty: Hard' />

## approach:

- used Binary Search on answer to find minimum possible largest subarray sum
- set search range from max(nums) to sum(nums)
- for each middle value, greedily formed subarrays without exceeding current limit
- If array could be split into at most k subarrays, searche for a smaller limit
- otherwise, increase limit and continue the search
- final value is minimum possible largest subarray sum

- Time complexity: O(nlogn)
- Space complexity: O(1)

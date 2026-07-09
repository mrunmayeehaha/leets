<h2><a href="https://leetcode.com/problems/subarray-sum-equals-k">Subarray Sum Equals K</a></h2> <img src='https://img.shields.io/badge/Difficulty-Medium-orange' alt='Difficulty: Medium' />

## approach:


- started a subarray from every index
- extended the subarray one element at a time
- maintained a running sum
- if the running sum becomes k, increment the answer
- then repeat for every starting index

- Time complexity: O(n^2)
- Space complexity: O(1)

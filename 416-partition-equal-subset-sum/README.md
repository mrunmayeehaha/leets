<h2><a href="https://leetcode.com/problems/partition-equal-subset-sum">Partition Equal Subset Sum</a></h2> <img src='https://img.shields.io/badge/Difficulty-Medium-orange' alt='Difficulty: Medium' />

## approach:

- used 1D DP for subset sum
- find total sum of the array
- if total sum is odd, return False because it cannot be divided equally
- target = total // 2
- dp[t] means can we make sum t using the numbers processed so far
- set dp[0] = True because sum 0 is always possible
- for every number, check sums from target down to num
- if dp[t - num] is True, then dp[t] = True
- this means: if we can make t - num, then adding num makes t
- if dp[target] becomes True, return True
- otherwise return False

- Time complexity: O(n * target)
- Space complexity: O(target)

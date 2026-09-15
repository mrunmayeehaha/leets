<h2><a href="https://leetcode.com/problems/jump-game">Jump Game</a></h2> <img src='https://img.shields.io/badge/Difficulty-Medium-orange' alt='Difficulty: Medium' />

## Approach:

- keep track of the farthest index we can reach
- start with farthest = 0
- for every reachable index, calculate i + nums[i]
- update farthest with the maximum value
- if an index is greater than farthest, we cannot reach it, so return False
- if farthest reaches the last index, return True
- Greedy Invariant: farthest always stores the farthest index that can be reached from the positions processed so far
- Greedy Justification: reaching farther is always at least as good as reaching a smaller index, so we only need to keep the maximum reachable position
- Time Complexity: O(n)
- Space Complexity: O(1)


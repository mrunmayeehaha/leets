<h2><a href="https://leetcode.com/problems/combination-sum">Combination Sum</a></h2> <img src='https://img.shields.io/badge/Difficulty-Medium-orange' alt='Difficulty: Medium' />

## Approach:
used DFS + Backtracking.
- at every candidate, we have 2 choices: take it or skip it.
- if we take the candidate, call DFS with the same i because the same number can be used again.
- if we skip the candidate, move to i + 1.
- if total == target, add the current path to ans.
- if total > target or all candidates are checked, return.
- after taking a candidate, remove it from path after DFS, i.e. backtracking.
- continue until all possible combinations are checked.
- Time Complexity: O(2^N)
- Space Complexity: O(T)
where N = number of candidates and T = target.

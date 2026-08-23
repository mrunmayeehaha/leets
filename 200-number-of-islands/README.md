<h2><a href="https://leetcode.com/problems/number-of-islands">Number of Islands</a></h2> <img src='https://img.shields.io/badge/Difficulty-Medium-orange' alt='Difficulty: Medium' />

## approach:

- if theres no grid, return 0 as no island
- assign no. of rows ans columns, initialize count with 0
- in helper function dfs,
    - if current index is less than length of rows or cols, or more than length of rows and cols, or if the current index is water or already visited, then return i.e. stop recursion
    - else, mark element at current index as 0 i.e. it is visited
    - traverse to index below current 1, above the current 1, and left and right of the current 1
  - for in range of rows and cols, if current index is 1
       - increase count by 1
       - reiterate dfs helper function
- return count of islands

- Time complexity: O(m * n)
- Space complexity: O(m * n)

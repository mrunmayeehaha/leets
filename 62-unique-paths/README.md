<h2><a href="https://leetcode.com/problems/unique-paths">Unique Paths</a></h2> <img src='https://img.shields.io/badge/Difficulty-Medium-orange' alt='Difficulty: Medium' />

## approach:
- start with a grid of size m x n
- put 1 in the first row and first column because there is only one way to reach those cells (all right moves or all down moves)
- for every other cell (i, j) calculate ways by adding the value from the cell above (i-1, j) and the cell on the left (i, j-1)
- keep filling the grid row by row and column by column using this rule
- the bottom right cell will hold the total number of unique paths

- Time complexity: O(m * n)
- Space complexity: O(m * n)

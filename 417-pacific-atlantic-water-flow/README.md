<h2><a href="https://leetcode.com/problems/pacific-atlantic-water-flow">Pacific Atlantic Water Flow</a></h2> <img src='https://img.shields.io/badge/Difficulty-Medium-orange' alt='Difficulty: Medium' />

## approach:

- used DFS + sets
- created 2 sets: pacific and atlantic
- started DFS from all Pacific border cells
- started DFS from all Atlantic border cells
- in DFS, moved to a cell only if heights[nr][nc] >= heights[r][c]
- this finds all cells from which water can reach each ocean
- returned the intersection of both sets

- Time complexity: O(m × n)
- Space complexity: O(m × n)

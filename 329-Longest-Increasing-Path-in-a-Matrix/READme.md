## Approach:
- use DFS to explore increasing paths from each cell
- use memoization to store the longest increasing path starting from each cell
- try all 4 directions from the current cell
- move only if the next cell has a greater value
- add 1 for the current cell to the path length returned by DFS
- store the calculated length in memo to avoid repeated work
- run DFS from every cell and keep the maximum length
- Time Complexity: O(m × n)
- Space Complexity: O(m × n)

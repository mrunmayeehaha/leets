<h2><a href="https://leetcode.com/problems/word-search">Word Search</a></h2> <img src='https://img.shields.io/badge/Difficulty-Medium-orange' alt='Difficulty: Medium' />

## Approach:
- used DFS + Backtracking.
- check every cell as a possible starting point of the word.
- tells which character of the word I need to find.
- If the current cell is outside the board, or doesn't match word[i], return False.
- If i == len(word), the complete word is found, return True.
- mark the current cell as # so same cell int used again
- check up, down, left, right using DFS.
- After checking, restore the cell i.e. backtracking.
If any path finds the complete word, return True; otherwise False.


- Time Complexity: O(m × n × 4^L)
- Space Complexity: O(L)

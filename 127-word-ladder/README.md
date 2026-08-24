<h2><a href="https://leetcode.com/problems/word-ladder">Word Ladder</a></h2> <img src='https://img.shields.io/badge/Difficulty-Hard-red' alt='Difficulty: Hard' />

## approach:

- Start with beginWord. Put it in a queue with step = 1
- Keep a set of all words from dictionary for fast lookup
- While queue not empty → pop one word
- If that word == endWord → return its step count
- Else, generate all possible one‑letter changes
- If new word exists in set → push into queue with step+1, and remove from set (visited)
- Continue BFS till queue empty
- If never found endWord → return 0

- Time complexity: O(N * L * 26)
- Space complexity: O(N)

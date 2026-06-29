<h2><a href="https://leetcode.com/problems/merge-strings-alternately">Merge Strings Alternately</a></h2> <img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' />

## approach:


- Created empty string result
- Traversed through word1 and word2 using for loop with i initialized to 0
- If i less than length of word1, add to result
- If i less than length of word2, add to result
- Return result when both strings end

- Time comlexity: O((m + n)^2)
- Space complexity: O(m + n)

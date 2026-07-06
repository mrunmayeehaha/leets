<h2><a href="https://leetcode.com/problems/find-words-that-can-be-formed-by-characters">Find Words That Can Be Formed by Characters</a></h2> <img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' />

## approach:


- imported Counter from the collections module
- stored frequency of characters in chars using chars_count and initialized total = 0
- iterated through each word in words and stored its character frequency in words_count
- compared the frequency of every character in words_count with chars_count
- if word can be formed then added its frequency total
- return total

- Time complexity: O(c + w)
- Space complexity: O(1)

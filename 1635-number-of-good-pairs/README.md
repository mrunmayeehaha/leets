<h2><a href="https://leetcode.com/problems/number-of-good-pairs">Number of Good Pairs</a></h2> <img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' />

## approach:


- Initialized count variable to 0
- Iterating through array using 'i', starting from 0th index
- For each i, iterated through remaining elements using j, strartig from i + 1
- If element at indices i and j are equal, increment count by 1
- return count after checcking all pairs

- Time Complexity: O(n^2)
- Space Complextiy: O(1)

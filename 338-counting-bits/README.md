<h2><a href="https://leetcode.com/problems/counting-bits">Counting Bits</a></h2> <img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' />

## approach:

- used DP + bit manipulation
- i >> 1 removes the last bit of i
- i & 1 checks whether the last bit is 1
- reuse the already calculated answer for i >> 1

- Time complexity: O(n)
- Space complexity: O(n)

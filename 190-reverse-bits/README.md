<h2><a href="https://leetcode.com/problems/reverse-bits">Reverse Bits</a></h2> <img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' />

## approach:

- take the last bit of n using n & 1
- shift ans left by 1 and put the extracted bit using | bit
- shift n right by 1 to remove its last bit
- repeat this process for all 32 bits
- return ans after all bits are reversed
- Time Complexity: O(1)
- Space Complexity: O(1)

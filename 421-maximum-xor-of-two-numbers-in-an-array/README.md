
<h2><a href="https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array">Maximum XOR of Two Numbers in an Array</a></h2> <img src='https://img.shields.io/badge/Difficulty-Medium-orange' alt='Difficulty: Medium' />

## approach:

- used Binary Trie to store bits of all numbers
- store each number from bit 30 to bit 0
- for every number, check its bits again
- try to take the opposite bit to get 1 in XOR
- if opposite bit is not present, take the same bit
- keep the maximum XOR found

- Time Complexity: O(31 × n) → O(n)
- Space Complexity: O(31 × n) → O(n)

<h2><a href="https://leetcode.com/problems/power-of-two">Power of Two</a></h2> <img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' />

## approach:

- first find the XOR of a and b because XOR gives the sum without carry
- find the carry using a & b
- left shift the carry by 1 because carry moves to the next bit
- repeat this until there is no carry left
- the final value of a is the answer
- Time Complexity: O(1)
- Space Complexity: O(1)

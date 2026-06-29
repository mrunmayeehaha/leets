<h2><a href="https://leetcode.com/problems/move-zeroes">Move Zeroes</a></h2> <img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' />

## approach:


- initialized k to 0 to keep track of from where non zero numbers should be placed
- traversing through list using for loop
- If current element is non zero then place it at index k and increment k
- After moving all non zero numbers, filled remaining positions with 0 with while loop
- Original array is modified

- Time complexity: O(n)
- Space complexity: O(1)

<h2><a href="https://leetcode.com/problems/max-consecutive-ones">Max Consecutive Ones</a></h2> <img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' />

## approach:


- Initialized max, count to 0
- Traversing thorugh  array by for loop
    - If current number equal to 1, increment count
    - If count greater than max, assign count to max
    - Else, count equal 0
Return max

Time complexity: O(n)
Space complexity: O(1)

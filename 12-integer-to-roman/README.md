<h2><a href="https://leetcode.com/problems/integer-to-roman">Integer to Roman</a></h2> <img src='https://img.shields.io/badge/Difficulty-Medium-orange' alt='Difficulty: Medium' />

## approach:


- created empty string ans
- created parallel arrays values with integer values and symbols with roman values
- iterated through values with for loop
    - while num is greater than or equal to current value
        - added correcponding roman symbol to ans
        - subtraced current value from num
- return ans

- Time complexity: O(1)
- Space complexity: O(1)

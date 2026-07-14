<h2><a href="https://leetcode.com/problems/roman-to-integer">Roman to Integer</a></h2> <img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' />

## approach:

- initialzed ans with 0
- created dictionary with each roman and integer as pairs
- iterated through given string with for loop
     - if current character was lesser than next character as per dictionary, subtract from current ans value
     - else, add it to ans
- add the last character to ans
- return ans

- Time complexity: O(n)
- Space complexity: O(1)

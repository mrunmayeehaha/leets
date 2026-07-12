<h2><a href="https://leetcode.com/problems/valid-parentheses">Valid Parentheses</a></h2> <img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' />

## approach:


- created dictionary pairs with each opening bracket as key and closing as value
- created empty stack
- traversed through given string using for loop
    - if character is an opening bracket, append in stack
    - else,
        - if stack is empty or top bracket in stack doesnt match to corresponding opening bracket only, return false 
- return true if length of stack equal 0

- Time complexity: O(n)
- Space complexity: O(n)

<h2><a href="https://leetcode.com/problems/valid-palindrome">Valid Palindrome</a></h2> <img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' />
approach:
I converted string to list tto access index by index
Started 'left' pointer from  1st element and 'right' pointer from last and moving them towards each other until middle character
Used isalnum() to check if a character is alphabet,digit and not any symbol
If symbol or space then go to next character
If characters converted in lowercase not equal, return false
Else to next character, check, after left pointer becomes equal or greater than right, end loop return true or false.

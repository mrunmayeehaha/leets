<h2><a href="https://leetcode.com/problems/reverse-vowels-of-a-string">Reverse Vowels of a String</a></h2> <img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' />

## approach:


-  Stored all uppercase and lowercase vowels in a set vowels 
- Converted string to list so its characters could be modified
- Initialized 2 pointers: left at beginning and right at the end of list
- While left is less than right,
   - If element at left was not vowel, increment left
   - Else if element at right was not a vowel, decrement right
   - Else, swap the characters at left and riht, then increment left and decrement right
- Joined the list back into a string and returned it.

- Time complexity: O(n)
- Space complexity: O(n)

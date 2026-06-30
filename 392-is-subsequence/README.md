<h2><a href="https://leetcode.com/problems/is-subsequence">Is Subsequence</a></h2> <img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' />

## approach:


- Iniitialized i,j to 0
- While i is less than length of string s and  j is less than length of string t:
    - If s[i] is equal to [j], increment i
    - Increment j to move to next character in string t
- Return True if i equal to length of string s, else return False

- Time complexity: O(s + t)
- Space complexity: O(1)

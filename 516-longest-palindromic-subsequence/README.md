<h2><a href="https://leetcode.com/problems/longest-palindromic-subsequence">Longest Palindromic Subsequence</a></h2> <img src='https://img.shields.io/badge/Difficulty-Medium-orange' alt='Difficulty: Medium' />

## approach:

- start with single letters,  each one is a palindrome of length 1
- then expand to pairs, if both ends match, length = 2, else take the bigger of the two sides
- then expand to longer substrings, keep checking ends:
- if ends match, add 2 + result of inside substring
- if ends don’t match, take max of ignoring left or right end
- keep filling the dp table step by step until the whole string is covered
- final cell dp[0][n-1] gives the longest palindromic subsequence length

- Time complexity: O(n^2)
- Space complexity: O(n^2)

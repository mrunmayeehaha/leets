<h2><a href="https://leetcode.com/problems/word-break">Word Break</a></h2> <img src='https://img.shields.io/badge/Difficulty-Medium-orange' alt='Difficulty: Medium' />>

## approach:

- used 1D DP
- dp[i] means first i characters of s can be formed using words from wordDict
- set dp[0] = True because an empty string can be formed
- for every position i, check every word in wordDict
- if the word can fit before i and dp[i - len(word)] is True, check whether that substring equals the word
- if it matches, set dp[i] = True
- finally, return dp[len(s)]
- Time Complexity: O(n * m * k)
- Space complexity: O(n)

<h2><a href="https://leetcode.com/problems/longest-substring-without-repeating-characters">Longest Substring Without Repeating Characters</a></h2> <img src='https://img.shields.io/badge/Difficulty-Medium-orange' alt='Difficulty: Medium' />

## approach:


- used two pointers left and right to maintain window of characters
- used a set to store characters currently present in the window
- moved the right pointer through the string and added characters to the set if they are not already present
- if a duplicate character is found, moved the left pointer forward and removed characters from the set until the 
  duplicate is removed
- after every valid window, calculate its length and update maximum length so far
- return maximum length after traversing entire string

- Time Complexity: O(n)  
- Space Complexity: O(k)  

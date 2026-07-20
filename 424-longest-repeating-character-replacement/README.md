<h2><a href="https://leetcode.com/problems/longest-repeating-character-replacement">Longest Repeating Character Replacement</a></h2> <img src='https://img.shields.io/badge/Difficulty-Medium-orange' alt='Difficulty: Medium' />

## approach:
- Used a sliding window with two pointers left and right
- Maintained a frequency map for characters inside the current window
- Tracked the maximum frequency (maxFreq) of any character in the window
- Expanded the window by moving right and updating the frequency map
- If the number of characters that needed replacement (window size - maxFreq) exceeded k, shrank the window by moving left
- Updated the maximum window length whenever the current window was valid
- Returned the length of the longest valid window

- Time complexity: O(n)
- Space complexity: O(1)

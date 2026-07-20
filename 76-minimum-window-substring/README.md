<h2><a href="https://leetcode.com/problems/minimum-window-substring">Minimum Window Substring</a></h2> <img src='https://img.shields.io/badge/Difficulty-Hard-red' alt='Difficulty: Hard' />

## approach:

- Created a frequency map need for string t to keep track of how many of each character are still required
- Used a variable-size sliding window with left and right pointers
- Expanded the window by moving right:
    - If the current character is required, decreased its frequency in need
    - If its frequency remained >= 0 after decrementing, increased count because a required character was matched
- When count == len(t), the current window contained all required characters
- Shrank the window from the left while it remained valid:
     - Updated the minimum window if the current one was smaller
     - Before moving left, restored the frequency of s[left] in need
     - If restoring made the frequency > 0, decreased count because a required character was removed from the window
- Continued expanding and shrinking until the entire string was processed
- Returned the smallest valid window, or an empty string if no valid window existed
  
- Time complexity: O(m + n)
- Space complexity: O(1)

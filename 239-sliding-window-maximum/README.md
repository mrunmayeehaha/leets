<h2><a href="https://leetcode.com/problems/sliding-window-maximum">Sliding Window Maximum</a></h2> <img src='https://img.shields.io/badge/Difficulty-Hard-red' alt='Difficulty: Hard' />

## approach:


- Used a monotonic decreasing deque to store indices of useful elements for the current window
- Before adding a new element, removed all smaller elements from the back since they can never become the maximum while the current element is in the window
- Added the current index to the deque
- Removed the front index if it was outside the current window
- Once the first window of size k was formed, appended the value at the front of the deque as the maximum
- Repeated the process until all windows were processed

- Time complexity: O(n)
- Space complexity: O(k)

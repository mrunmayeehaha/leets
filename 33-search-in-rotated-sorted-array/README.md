<h2><a href="https://leetcode.com/problems/search-in-rotated-sorted-array">Search in Rotated Sorted Array</a></h2> <img src='https://img.shields.io/badge/Difficulty-Medium-orange' alt='Difficulty: Medium' />

## approach:

- initialize left to 0 and right to last element
- while left less than or equal to right
     - check if element at mid is equal to target, if yes return the position of mid
     - if number at left's position is less than or equal to mid (means left side sorted)
          - check for target between left and mid, right equal mid - 1
          - else, left equal mid + 1
     - else, (if right side sorted)
         - check for target between mid and last element, if present then left equal mid + 1
         - else, right equal mid - 1
- if target not present, return -1

- Time complexity: O(log n)
- Space complexity: O(1)


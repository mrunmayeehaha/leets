<h2><a href="https://leetcode.com/problems/find-minimum-in-rotated-sorted-array">Find Minimum in Rotated Sorted Array</a></h2> <img src='https://img.shields.io/badge/Difficulty-Medium-orange' alt='Difficulty: Medium' />

## approach:

- initialize left and right to 0 and to last element respectively, minimum to 0
- while left is less than right, calculate mid
- if the number at mid is greater than number at last position, left side is sorted therefore left equals mid + 1
- else right equals mid i.e. right side sorted
- return nums[left]

- Time complexity: O(log n)
- Space complexity: O(1)

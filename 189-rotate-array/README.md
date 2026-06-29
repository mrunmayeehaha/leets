<h2><a href="https://leetcode.com/problems/rotate-array">Rotate Array</a></h2> <img src='https://img.shields.io/badge/Difficulty-Medium-orange' alt='Difficulty: Medium' />

## approach:


- Updated k by taking k % len(nums) to handle cases where k is greater than the length of the array
- Extracted the last k elements of the array using slicing
- Extracted the remaining elements from the beginning of the array
- Concatenated both parts to form the rotated array
- Assigned the rotated array back to nums using slice assignment (nums[:]) so the original list is modified in place

- Time complexity: O(n)
- Space complexity: O(n)

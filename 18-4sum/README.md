<h2><a href="https://leetcode.com/problems/4sum">4Sum</a></h2> <img src='https://img.shields.io/badge/Difficulty-Medium-orange' alt='Difficulty: Medium' />

## Approach

- sort the array.
- fix the first two elements using nested loops (i and j).
- use two pointers (left and right) to find the remaining two elements.
- calculate the sum of the four numbers:
  - if sum == target, store the quadruplet, move both pointers, and skip duplicates.
  - if sum < target, move left to increase the sum.
  - if sum > target, move right to decrease the sum.
- skip duplicate values for i, j, left, and right to avoid repeated quadruplets.

-Time Complexity: O(n³)
-Space Complexity: O(1) (excluding the output list)


- 

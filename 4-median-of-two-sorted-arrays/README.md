<h2><a href="https://leetcode.com/problems/median-of-two-sorted-arrays">Median of Two Sorted Arrays</a></h2> <img src='https://img.shields.io/badge/Difficulty-Hard-red' alt='Difficulty: Hard' />

## approach:

- combine both sorted arrays into a single array
- sort the merged array
- find middle index of the sorted array
- if total number of elements is odd, return middle element
- if total number of elements is even, return average of two middle elements

- Time complexity: O(log (m + n))
- Space complexity: O(1)

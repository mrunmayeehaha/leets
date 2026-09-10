<h2><a href="https://leetcode.com/problems/count-of-smaller-numbers-after-self">Count of Smaller Numbers After Self</a></h2> <img src='https://img.shields.io/badge/Difficulty-Hard-red' alt='Difficulty: Hard' />

## approach:

- used Fenwick Tree to count smaller numbers
- first sort the unique numbers and give them ranks
- process the array from right to left
- query(r - 1) gives the count of numbers smaller than current number
- update(r) adds the current number to the Fenwick Tree
- reverse ans because we processed from right to left

- Time Complexity: O(n log n)
- Space Complexity: O(n)

<h2><a href="https://leetcode.com/problems/candy">Candy</a></h2> <img src='https://img.shields.io/badge/Difficulty-Hard-red' alt='Difficulty: Hard' />

## approach:
- give every child 1 candy initially
- traverse from left to right
- if the current rating is greater than the left rating, give one more candy than the left child
- traverse from right to left
- if the current rating is greater than the right rating, give one more candy than the right child
- use max() so we don't decrease candies already given in the first pass
- add all the candies and return the total
- Greedy Invariant: after both passes, every child has enough candies to satisfy both neighbouring rating conditions
- Time complexity: O(n)
- Space complexity: O(n)

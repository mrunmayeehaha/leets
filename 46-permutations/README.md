<h2><a href="https://leetcode.com/problems/permutations">Permutations</a></h2> <img src='https://img.shields.io/badge/Difficulty-Medium-orange' alt='Difficulty: Medium' />

## approach:
- use backtracking to generate all possible permutations
- maintain a path list for the current permutation
- maintain a used array to check whether an element is already present in the current path
- loop through every element and choose it if it is not used
- add the element to path and mark it as used
- recursively continue building the permutation
- when path reaches the size of nums, add a copy of it to the answer
- remove the last element using pop() and mark it unused so other permutations can be tried

- time complexity: O(n * n!)
- Space complexity: O(n)

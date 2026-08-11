<h2><a href="https://leetcode.com/problems/subsets">Subsets</a></h2> <img src='https://img.shields.io/badge/Difficulty-Medium-orange' alt='Difficulty: Medium' />

## approach:
- use backtracking to generate all possible subsets
- maintain a path list for the current subset
- at every index, there are 2 choices: take the current element or skip it
- first add nums[i] to path and recursively continue
- then remove it using pop() and recursively continue without taking it
- when i reaches len(nums), all elements have been considered, so add the current path to ans
- this generates every possible combination of taking or skipping each element

## complexity:
- time complexity: O(n × 2^n)
- space complexity: O(n)
- output space: O(n × 2^n)

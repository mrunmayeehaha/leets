<h2><a href="https://leetcode.com/problems/next-greater-element-i">Next Greater Element I</a></h2> <img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' />

## approach:


- Created an empty stack and a dictionary next_greater
- Traversed nums2 using a for loop 
   - While the stack was not empty and the current element was greater than the top element of the stack:
       - Popped the top element from the stack
       - Stored the current element as its next greater element in the dictionary
   - Pushed the current element onto the stack
- After traversing nums2, assigned -1 as the next greater element for all remaining elements in the stack
- Created an empty list result
- Traversed nums1 and appended the corresponding next greater element from the dictionary to result
- Returned result

- Time complexity: O(n + m)
- Space complexity: O(n)

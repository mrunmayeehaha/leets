<h2><a href="https://leetcode.com/problems/longest-consecutive-sequence">Longest Consecutive Sequence</a></h2> <img src='https://img.shields.io/badge/Difficulty-Medium-orange' alt='Difficulty: Medium' />

## approach:


- initialized i, current, longest to 0
- if array is empty, return 0
- sort the given array
- traversed through the array using for loop,
     - if the difference of current number and the next number is equal to 1, then increment current
     - if current number and next number are same,skip the number
     - else, assign highest number amongst longest and current to current, initialize current to 1(this is when sequence 
       breaks)
- assign greater count to longest
- return longest

- Time complexity: O(n)
- Space complexity: O(1)

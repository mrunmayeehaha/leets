<h2><a href="https://leetcode.com/problems/climbing-stairs">Climbing Stairs</a></h2> <img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' />

## approach:
- if no. of stairs is 1, return 1 cuz there is only 1 way for climbing it
- else, create array initialized with 0 at each element
- initialize no. of ways for climbing 1 and 2 stairs as 1 and 2 as they are fixed
- for loop always start with 3 (as we have 1 and 2),
- for each step calculate ways backwards for 1 and 2 and it addition will be number of ways for that current step
- return no. of ways at n i.e. asked step

- time complexity: O(n)
- Space complexity: O(n)

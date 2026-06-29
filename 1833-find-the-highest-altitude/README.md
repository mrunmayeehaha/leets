<h2><a href="https://leetcode.com/problems/find-the-highest-altitude">Find the Highest Altitude</a></h2> <img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' />

## approach:


- Initialized variables highest, altitude and i to 0
- Iterating through gain array i is less than length 
- Adding current gain value to altitude
- If altitude becomes greater than highest, assign updated highest to altitude
- increment i after each iteration
- return highest after traversing entire array

- Time Complexity: O(n)
- Space Complexity: O(1)

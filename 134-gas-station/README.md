<h2><a href="https://leetcode.com/problems/gas-station">Gas Station</a></h2> <img src='https://img.shields.io/badge/Difficulty-Medium-orange' alt='Difficulty: Medium' />

## approach:
- calculate the gas we gain or lose at each station using gas[i] - cost[i]
- keep track of total gas and tank gas
- total tells us if completing the whole circuit is possible
- tank tells us whether our current starting point is still possible
- if tank becomes negative, current start cannot work
- set the next station as new starting point and reset tank = 0
- if total < 0, return -1
- otherwise, return the start index
- Greedy Invariant: if a starting point fails at station i, no station between that start and i can be a valid starting point
- Time complexity: O(n)
- Space complexity: O(1)

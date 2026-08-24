<h2><a href="https://leetcode.com/problems/course-schedule">Course Schedule</a></h2> <img src='https://img.shields.io/badge/Difficulty-Medium-orange' alt='Difficulty: Medium' />

## approach:

- create graph and empty list for every course
- add course to graph[pre]
- create state array with all 0
- make DFS function
- if state[course] == 1, forms cycle therefore False
- if state[course] == 2, already checked therefore True
- mark current course as 1
- DFS all its next courses
- if any DFS returns False, return False
- mark course as 2 after checking all neighbours
- run DFS for every course
- if no cycle, return True

- Time complexity: O(V + E)
- Space complexity: O(V + E)

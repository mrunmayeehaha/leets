<h2><a href="https://leetcode.com/problems/clone-graph">Clone Graph</a></h2> <img src='https://img.shields.io/badge/Difficulty-Medium-orange' alt='Difficulty: Medium' />

## approach:

- if no node given, return none
- create empty dictionary to keep check which nodes are visited
- in helper function dfs
    - if any value in dictionary, return current value
    - else, assign variable copy with current node value
    - put that value to that same index no. in dictionary
    - traverse through values connected to the current node, and add the cloned neighbours to current node's neighbour list if copy isnt created
    - else, return copy

 - Time complexity: O(V + E)
 - Space complexity: O(V)

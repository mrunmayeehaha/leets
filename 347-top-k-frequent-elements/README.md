<h2><a href="https://leetcode.com/problems/top-k-frequent-elements">Top K Frequent Elements</a></h2> <img src='https://img.shields.io/badge/Difficulty-Medium-orange' alt='Difficulty: Medium' />

## approach:

- import Counter for frequency count and heapq for minheap
- declare heap empty array
- for num(actual no.) and count(frequency) in kay and value
     - push the number and its frequency in heap array
     - if length of heap array becomes more than k
          - pop the number and count of least frequency
- from the remaining num, count elements in heap array return only its actual number part i.e. 'num'

- Time complexity: O(n logk)
- Space complexity: O(n)

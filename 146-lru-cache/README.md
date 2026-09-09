<h2><a href="https://leetcode.com/problems/lru-cache">LRU Cache</a></h2> <img src='https://img.shields.io/badge/Difficulty-Medium-orange' alt='Difficulty: Medium' />

## approach:

- HashMap + Doubly Linked List
- HashMap, finds key in O(1) 
- DLL, maintains recent usage order 
- head.next = Least Recently Used 
- tail.prev = Most Recently Used 
- get() - node find and move to end
- put() - add/update then move to end then if capacity exceeds head.next delete

- Time: O(1) for both get() and put()
- Space: O(capacity)

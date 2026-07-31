<h2><a href="https://leetcode.com/problems/linked-list-cycle">Linked List Cycle</a></h2> <img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' />

## approach:

- keep slow and fast at head
- move slow one step at a time
- move fast two steps at a time
- if both pointers meet, a cycle exists
- if fast reaches None, no cycle exists

## Complexity:
time: O(n)
space: O(1)

## Pointer Diagram:
1 → 2 → 3 → 4
     ↑     ↓
slow  one step
fast   two steps
slow == fast

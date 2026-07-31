<h2><a href="https://leetcode.com/problems/reverse-linked-list">Reverse Linked List</a></h2> <img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' />

## approach:

-initialize prev = None and curr = head
-save curr.next in nextNode
- point curr.next to prev
- move prev to curr
- move curr to nextNode
- repeat until curr becomes None
- return prev

## Complexity:
time: O(n)
space: O(1)

## pointer diagram:
prev    curr
 ↓       ↓
None    1 → 2 → 3

nextNode
   ↓
2 → 3

curr.next = prev
1 → None

prev      curr
 ↓         ↓
1 → None   2 → 3

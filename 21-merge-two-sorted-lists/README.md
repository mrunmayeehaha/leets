<h2><a href="https://leetcode.com/problems/merge-two-sorted-lists">Merge Two Sorted Lists</a></h2> <img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' />

## approach:
- create a dummy node and keep curr pointing to it
- compare values from both lists
- attach the smaller node to curr.next
- move curr and the selected list forward
- repeat until one list ends
- attach the remaining nodes
- return dummy.next

## Complexity:
time: O(n + m)
space: O(1)

## Pointer Diagram:
List1
1 → 3 → 5
List2
2 → 4 → 6
dummy
0 → 1 → 2 → 3 → 4 → 5 → 6

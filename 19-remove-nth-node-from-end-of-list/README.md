<h2><a href="https://leetcode.com/problems/remove-nth-node-from-end-of-list">Remove Nth Node From End of List</a></h2> <img src='https://img.shields.io/badge/Difficulty-Medium-orange' alt='Difficulty: Medium' />

## Approach:
- find the length of the linked list
- calculate target = length - n
i- f target == 0, return head.next
- move curr until it reaches target - 1
- remove the target node using curr.next = curr.next.next
- return head

## Complexity:
time: O(n)
space: O(1)

## Pointer Diagram:
1 → 2 → 3 → 4 → 5
target = index 3
curr
 ↓
1 → 2 → 3 → 4 → 5
curr.next = curr.next.next
1 → 2 → 3 → 5

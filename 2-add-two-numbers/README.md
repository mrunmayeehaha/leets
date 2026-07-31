<h2><a href="https://leetcode.com/problems/add-two-numbers">Add Two Numbers</a></h2> <img src='https://img.shields.io/badge/Difficulty-Medium-orange' alt='Difficulty: Medium' />

## Approach:

- create a dummy node and keep curr at it
- initialize carry = 0
- keep traversing while l1, l2, or carry exists
- add both digits and the carry
- store total % 10 in a new node
- update carry = total // 10
- move all pointers forward
- return dummy.next

## Complexity:
- time: O(max(n, m))
- space: O(max(n, m))

## Pointer Diagram:
l1
2 → 4 → 3

l2
5 → 6 → 4

2 + 5 + 0 = 7

answer
7
4 + 6 + 0 = 10
answer
7 → 0
carry = 1
3 + 4 + 1 = 8
answer
7 → 0 → 8

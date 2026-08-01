<h2><a href="https://leetcode.com/problems/invert-binary-tree">Invert Binary Tree</a></h2> <img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' />

## approach:

- start from the root node.
- if the node is null, stop the recursion.
- swap the left and right child of the current node.
- recursively invert the left subtree.
- recursively invert the right subtree.
- return the root after all nodes have been processed.

## complexity:
- Time: O(n)
- Space: O(h)

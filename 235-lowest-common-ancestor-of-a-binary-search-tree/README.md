<h2><a href="https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree">Lowest Common Ancestor of a Binary Search Tree</a></h2> <img src='https://img.shields.io/badge/Difficulty-Medium-orange' alt='Difficulty: Medium' />

## approach:

- Start from the root of the BST
- If both p and q have values smaller than the current node, move to the left subtree
- If both p and q have values greater than the current node, move to the right subtree
- Otherwise, the current node is the first point where the paths to p and q split (or one of them is the current node), so it is the Lowest Common Ancestor

- Time complexity: O(h)
- Space complexity: O(h)

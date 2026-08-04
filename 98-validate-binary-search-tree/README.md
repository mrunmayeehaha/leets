<h2><a href="https://leetcode.com/problems/validate-binary-search-tree">Validate Binary Search Tree</a></h2> <img src='https://img.shields.io/badge/Difficulty-Medium-orange' alt='Difficulty: Medium' />

## approach:

- create a helper function bst(node, low, high) where,
- node is the current node
- low is the minimum value the node can have
- high is the maximum value the node can have
- If the current node is None, return True because empty subtree is always a valid BST
- check whether current node's value lies between low and high. If it doesn't, return False since it violates the BST property
- If the current node is valid, recursively check
- The left subtree by keeping the same low and updating high to the current node's value
- The right subtree by updating low to the current node's value and keeping the same high
- Finally return the logical AND of both recursive calls. If both left and right subtrees are valid, the entire tree is a valid BST

- Time complexity: O(n)
- Space complexity: O(h)

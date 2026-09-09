<h2><a href="https://leetcode.com/problems/implement-trie-prefix-tree">Implement Trie (Prefix Tree)</a></h2> <img src='https://img.shields.io/badge/Difficulty-Medium-orange' alt='Difficulty: Medium' />

## approach:

- Created a TrieNode with children and isEnd
- children stores the next characters
- isEnd tells whether a complete word ends at that node
- insert(), goes character wise and create nodes if needed
- search(), traverse all characters and check isEnd 
- startsWith(), traverse the prefix; if all characters exist, return True 

- Time: O(L) for insert search and startsWith
- Space: O(N) for stored characters 

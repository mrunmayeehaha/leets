<h2><a href="https://leetcode.com/problems/lfu-cache">LFU Cache</a></h2> <img src='https://img.shields.io/badge/Difficulty-Hard-red' alt='Difficulty: Hard' />

## approach:

- Store key and value using HashMap
- Store the frequency of each key
- Group keys according to their frequency using OrderedDict
- On get(), increase the key's frequency
- On put(), if cache is full, remove least frequently used key
- If two keys have same frequency, remove least recently used key

- Time: O(1)
- Space: O(capacity)

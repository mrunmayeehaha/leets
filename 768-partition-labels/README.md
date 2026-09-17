<h2><a href="https://leetcode.com/problems/partition-labels">Partition Labels</a></h2> <img src='https://img.shields.io/badge/Difficulty-Medium-orange' alt='Difficulty: Medium' />

## appraoch:
- store the last occurrence of every character in a dictionary
- keep start for the beginning of the current partition
- keep end for the farthest last occurrence we need to reach
- traverse the string and update end using the last occurrence of current character
- when i == end, all occurrences of the characters in the current partition are completed, so we can make a partition
- add the partition length to the result and start a new partition
- Greedy: make the partition as soon as it is safe to do so, which gives the maximum number of partitions
- Time complexity: O(n)
- Space complexity: O(k) (k = number of distinct characters)


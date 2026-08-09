<h2><a href="https://leetcode.com/problems/find-median-from-data-stream">Find Median from Data Stream</a></h2> <img src='https://img.shields.io/badge/Difficulty-Hard-red' alt='Difficulty: Hard' />

## approach:

- used two heaps to keep track of the smaller and larger halves of numbers.
     - maxHeap stores smaller half.
     - minHeap stores larger half.
- Since Python's heapq only provides a min-heap, store negative values in maxHeap to use it as max-heap.
- Whenever a new number is added,put it into appropriate heap.
- then balance the two heaps so that their sizes never differ by more than 1.
- If both heaps have the same number of elements, the median is the average of their top elements.
- Otherwise, top of the larger heap is median.

- Time complexity: O(n logn)
- Space complexity: O(n)

<h2><a href="https://leetcode.com/problems/product-of-array-except-self">Product of Array Except Self</a></h2> <img src='https://img.shields.io/badge/Difficulty-Medium-orange' alt='Difficulty: Medium' />

## approach:


- initialized an answer array of size n with all elements as 1
- Traversed the array from left to right while maintaining a variable left to store the product of all elements to the - left of the current index
     - Stored the current left product in answer[i]
     - Updated left by multiplying it with the current element
- Traversed the array from right to left while maintaining a variable right to store the product of all elements to the right of the current index
     - Multiplied answer[i] with the current right product
     - Updated right by multiplying it with the current element
- Returned the answer array containing the product of all elements except the element at each index

- Time complexity: O(n)
- space complexity: O(1)

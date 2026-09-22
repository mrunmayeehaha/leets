<h2><a href="https://leetcode.com/problems/basic-calculator-ii">Basic Calculator II</a></h2> <img src='https://img.shields.io/badge/Difficulty-Medium-orange' alt='Difficulty: Medium' />

## approach:

- scan the string from left to right and build the complete number including multi-digit numbers
- keep a sign variable to remember the operator before the current number
- for +, add the number to the stack
- for -, add the negative of the number to the stack
- for *, multiply the last stack element with the current number
- for /, divide the last stack element by the current number and truncate toward zero
- add a dummy + at the end so the last number also gets processed
- finally, return sum(stack) because subtraction is already stored as negative values
- Time complexity: O(n)
- Space complexity: O(n)

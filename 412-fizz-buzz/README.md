<h2><a href="https://leetcode.com/problems/fizz-buzz">Fizz Buzz</a></h2> <img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' />

## approach:


- Created empty list answer
- Traversed whole given list through for loop
   - If element at current index was divisible by 3 and 5 both, append "FizzBuzz"
   - Else if current number divisible by 3, append "Fizz"
   - Else if current number divisible by 5, append "Buzz"
   - Else append str(i) i.e. current number as string
- Return answer

- Time complexity: O(n)
- Space complexity: O(n)

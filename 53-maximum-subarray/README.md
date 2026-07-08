<h2><a href="https://leetcode.com/problems/maximum-subarray">Maximum Subarray</a></h2> <img src='https://img.shields.io/badge/Difficulty-Medium-orange' alt='Difficulty: Medium' />

## approach:


- initialized currsum and maxsum with the first element of the array
- traversed the array from the second element onwards
- For each element:
     - compared extending the current subarray (currSum + nums[i]) with starting a new subarray from the current element 
       (nums[i])
- updated currsum with whichever value was larger
- if currsum was greater than maxSum, updated maxSum
- returned maxsum as the maximum subarray sum

- Time complexity: O(n)
- Space complexity: O(1)

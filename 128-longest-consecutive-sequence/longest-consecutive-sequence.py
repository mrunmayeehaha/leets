class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        i = 0
        current = 1
        longest = 1
        if not nums:
            return 0
        nums.sort()
        for i in range(len(nums) - 1):
            
            if nums[i + 1] - nums[i] == 1:
                current = current + 1
            elif nums[i + 1] == nums[i]:
                continue
            else:
                longest = max(longest,current)
                current = 1  
        longest = max(longest,current)
        return longest

        
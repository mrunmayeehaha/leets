class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currsum = nums[0]
        maxsum = nums[0]

        for i in range(1, len(nums)):
            if currsum + nums[i] > nums[i]:
                currsum = currsum + nums[i]
            else:
                currsum = nums[i]

            if currsum > maxsum:
                maxsum = currsum

        return maxsum
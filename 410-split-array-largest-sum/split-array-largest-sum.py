class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:

        def canSplit(limit):
            count = 1          #at least one subarray
            currSum = 0
            for num in nums:
                if currSum + num <= limit:
                    currSum += num
                else:
                    count += 1
                    currSum = num
            return count <= k

        left = max(nums)
        right = sum(nums)
        while left <= right:
            mid = (left + right) // 2
            if canSplit(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left
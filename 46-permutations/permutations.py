class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        path = []
        ans = []
        used = [False] * len(nums)

        def backtrack():
            if len(path) == len(nums):
                ans.append(path[:])
                return

            for i in range(len(nums)):
                if not used[i]:
                    path.append(nums[i])
                    used[i] = True
                    backtrack()
                    path.pop()
                    used[i] = False

        backtrack()
        return ans
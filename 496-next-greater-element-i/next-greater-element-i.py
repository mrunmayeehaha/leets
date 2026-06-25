class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        next_greater = {}
        for i in nums2:
            while stack and i > stack[-1]:
                next_greater[stack.pop()] = i
            stack.append(i)
        while stack:
            next_greater[stack.pop()] = -1
        result = []
        for i in nums1:
            result.append(next_greater[i])
        return result        
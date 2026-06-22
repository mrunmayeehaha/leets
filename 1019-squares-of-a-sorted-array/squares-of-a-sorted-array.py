class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]: 
        op= []
        for i in nums:
            i = i * i
            op.append(i)
        op.sort()
        return op

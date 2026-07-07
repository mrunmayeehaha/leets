from collections import Counter

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        count = Counter(nums)
        i = 0
        for i in count:
            if count[i] >= 2:
                return True
        return False

                
        
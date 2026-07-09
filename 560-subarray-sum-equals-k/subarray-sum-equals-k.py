from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        prefix = 0
        count = 0
        hashmap = defaultdict(int)
        hashmap[0] = 1      
        for num in nums:
            prefix += num
            need = prefix - k

            count += hashmap[need]
            hashmap[prefix] += 1

        return count
class Solution:
    def countSmaller(self, nums):

        sorted_nums = sorted(set(nums))
        rank = {num: i + 1 for i, num in enumerate(sorted_nums)}

        bit = [0] * (len(sorted_nums) + 1)

        def update(i):
            while i < len(bit):
                bit[i] += 1
                i += i & -i

        def query(i):
            total = 0

            while i > 0:
                total += bit[i]
                i -= i & -i

            return total

        ans = []

        for i in range(len(nums) - 1, -1, -1):
            r = rank[nums[i]]

            ans.append(query(r - 1))
            update(r)

        return ans[::-1]
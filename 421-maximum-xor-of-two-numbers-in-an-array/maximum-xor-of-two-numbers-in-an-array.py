class Solution:
    def findMaximumXOR(self, nums):
        trie = [[-1, -1]]

        for num in nums:
            node = 0

            for i in range(30, -1, -1):
                bit = (num >> i) & 1

                if trie[node][bit] == -1:
                    trie[node][bit] = len(trie)
                    trie.append([-1, -1])

                node = trie[node][bit]

        ans = 0

        for num in nums:
            node = 0
            curr = 0

            for i in range(30, -1, -1):
                bit = (num >> i) & 1
                opposite = 1 - bit

                if trie[node][opposite] != -1:
                    curr |= (1 << i)
                    node = trie[node][opposite]
                else:
                    node = trie[node][bit]

            ans = max(ans, curr)

        return ans


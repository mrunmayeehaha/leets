from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        left = 0
        count = 0

        start = 0
        minLen = float("inf")

        for right in range(len(s)):

            if s[right] in need:
                need[s[right]] -= 1

                if need[s[right]] >= 0:
                    count += 1

            while count == len(t):

                if right - left + 1 < minLen:
                    minLen = right - left + 1
                    start = left

                if s[left] in need:
                    need[s[left]] += 1

                    if need[s[left]] > 0:
                        count -= 1

                left += 1

        if minLen == float("inf"):
            return ""

        return s[start:start + minLen]
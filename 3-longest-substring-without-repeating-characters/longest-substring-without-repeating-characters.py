class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        count = 0
        sett = set()
        longest = 0
        left = 0
        right = 0
        for right in range(len(s)):
            if s[right] not in sett :
                sett.add(s[right])
                longest = max(longest, right - left + 1)

            else:
                while s[right] in sett:
                    sett.remove(s[left])
                    left += 1

                sett.add(s[right])
                longest = max(longest, right - left + 1)
                
        return longest
                
       
       
        longest = max(count, longest)
            
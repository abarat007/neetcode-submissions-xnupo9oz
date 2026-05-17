class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # if s is empty, return 0
        if len(s) == 0:
            return 0

        char_set = set()
        left = 0
        right = 0
        result = 0

        # s = "zxyzxyz"
        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(s[right])
            res = right - left + 1
            result = max(result, res)
        
        return result



            


        


        
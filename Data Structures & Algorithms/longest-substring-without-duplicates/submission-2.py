class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        chars_seen = set() # {x,y,z}
        n = len(s)
        max_len = 0 # 3
        # We can set up a variable right and loop through 's'
        for right in range(n):
            while s[right] in chars_seen:
                chars_seen.remove(s[left])
                left += 1
            
            chars_seen.add(s[right])
            max_len = max(max_len, right - left + 1)

        return max_len













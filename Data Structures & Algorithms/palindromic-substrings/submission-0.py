class Solution:
    def countSubstrings(self, s: str) -> int:
        # Brute force:
        # make a list of subsets strings, and then remove non-palindromic substrings

        # Palindromes can be odd or even length

        # aaa # odd len palindrome
        # # two pointers
        # left = center_idx
        # right = center_idx

        # caac # even len palindrome
        # # two pointers
        # left = center_idx
        # right = center_idx + 1

        # left = 0, right = 0 
        def expand(left, right):
            count = 0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
            return count

        res = 0
        # loop through the string and expand the left and right indices
        for i in range(len(s)):
            res += expand(i,i) # odd len palindrome
            res += expand(i, i+1) # even len palindrome
        
        return res






        
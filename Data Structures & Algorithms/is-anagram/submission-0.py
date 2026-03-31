class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        isAnagram = True
        # Base Case: if string lengths aren't equal, they can never be an anagram
        s_length = len(s)
        t_length = len(t)
        if s_length != t_length:
            return False
        
        # Other Cases

        # 1. We can start by setting 2 dictionaries to store the frequency of chars in both input strings
        s_dict = {}
        t_dict = {}

        # 2. We can loop through both strings
        for letter in s:
            if letter not in s_dict:
                s_dict[letter] = 1
            else:
                s_dict[letter] += 1
        
        for letter in t:
            if letter not in t_dict:
                t_dict[letter] = 1
            else:
                t_dict[letter] += 1
        
        # 3. Loop through each key in s_dict. Compare the value of that key to the same key in t_dict. If values are the same, continue the loop.
        # Otherwise, break the loop and return False
        for key, value in s_dict.items():
            if key not in t_dict or t_dict[key] != value:
                isAnagram = False
                break
            else:
                continue
        
        # 4. Return isAnagram
        return isAnagram
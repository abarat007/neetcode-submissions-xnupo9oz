class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        isPermutation = False
        s1_map = {}
        for char in s1:
            if char not in s1_map:
                s1_map[char] = 1
            else:
                s1_map[char] += 1
        
        # {a:1,b:1,c:1}
        window_len = len(s1) # 3

        for left in range(len(s2) - window_len + 1):
            window = s2[left:left + window_len]
            window_map = {}
            for c in window:
                window_map[c] = window_map.get(c, 0) + 1
            if window_map == s1_map:
                return True
        
        return False


                
            





        
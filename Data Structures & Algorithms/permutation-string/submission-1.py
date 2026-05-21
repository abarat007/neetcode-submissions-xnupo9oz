class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # base case
        if len(s1) > len(s2):
            return False
        
        valid = False
        window_size = len(s1) 

        s1_map = {}
        for char in s1:
            if char not in s1_map:
                s1_map[char] = 1
            else:
                s1_map[char] += 1
        
        # This gets all possible windows
        windows = [s2[i:i+window_size] for i in range(len(s2) - window_size + 1)]
        for window in windows:
            window_map = {}
            for char in window:
                if char not in window_map:
                    window_map[char] = 1
                else:
                    window_map[char] += 1
            if window_map == s1_map:
                return True
        
        return valid



        
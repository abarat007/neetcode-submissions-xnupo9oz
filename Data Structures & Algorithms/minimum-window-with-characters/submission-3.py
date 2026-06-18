class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        
        if s == t:
            return s

        t_map = {}
        for c in t:
            if c not in t_map:
                t_map[c] = 1
            else:
                t_map[c] += 1

        left = 0
        window_map = {}
        have = 0
        need = len(t_map)
        window_len = 0
        res_len = float('inf')
        res = []

        # s = "OUZODYXAZV", t = "XYZ"
        # Output: YXAZ

        for right in range(len(s)):
            c = s[right]
            if c not in window_map:
                window_map[c] = 1
            else:
                window_map[c] += 1
            if c in t_map and window_map[c] == t_map[c]:
                have += 1
            while have == need:
                window_len = right - left + 1
                if window_len < res_len:
                    res = [left,right]
                    res_len = window_len
                left_char = s[left]
                window_map[left_char] -= 1
                if left_char in t_map and window_map[left_char] < t_map[left_char]:
                    have -= 1
                left += 1

        return "" if res_len == float('inf') else s[res[0]:res[1]+1]

            
                    
        
        
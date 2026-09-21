class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_map = {}
        for s in strs:
            key = ''.join(sorted(s)) # key
            if key in str_map:
                str_map[key].append(s)
            else:
                str_map[key] = []
                str_map[key].append(s)
        
        res = []
        for val in str_map.values():
            res.append(val)
        
        return res


        
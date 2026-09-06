class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        n = len(s)
        
        char_map = {}
        # {char:last idx in s}

        for char in s:
            char_map[char] = char_map.get(char, 0)
        
        # print(char_map)

        for key in char_map.keys():
            target = key
            for i in range(n-1, -1, -1):
                if s[i] == target:
                    char_map[target] = i
                    break
        
        print(f'updated char map: \n{char_map}')
        
        res = []
        size = 0
        end = 0
        for idx, char in enumerate(s):
            size += 1
            end = max(end, char_map[char])
            if idx == end:
                res.append(size)
                size = 0
        return res



        
        


        




        
        
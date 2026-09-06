class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        n = len(s)
        
        char_map = {}
        # {char:last idx in s}

        for idx, char in enumerate(s):
            char_map[char] = idx
        
        # print(char_map)
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



        
        


        




        
        
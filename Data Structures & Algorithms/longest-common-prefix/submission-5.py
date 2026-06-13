class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix_list = []
        valid_char = True
        index = 0
        if not strs:
            return ""
        
        for c in strs[0]: # m i s m a t c h
            for word in range(1, len(strs)):
                if index >= len(strs[word]):
                    return ''.join(prefix_list)
                if c != strs[word][index]:
                    return ''.join(prefix_list)
                else:
                    continue
            prefix_list.append(c) # [m,i,s]
            index += 1

        return ''.join(prefix_list)

        



        
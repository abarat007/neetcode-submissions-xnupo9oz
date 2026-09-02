class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs]
        
        res = []

        anagram_sorted_map = defaultdict(list) # {ordered letters : strs}

        for word in strs:
            word_sorted = ''.join(sorted(word))
            anagram_sorted_map[word_sorted].append(word)
        
        for val in anagram_sorted_map.values():
            res.append(val)
        
        return res




        

        
            


            











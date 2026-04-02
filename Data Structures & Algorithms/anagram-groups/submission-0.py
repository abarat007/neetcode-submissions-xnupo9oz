class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Base Case: If len(strs) = 1, then we return the list itself
        if len(strs) == 1:
            return [strs]
        
        # Loop through strs and add sorted words together
        anagram_grouped = defaultdict(list)

        for word in strs:
            sorted_word = ''.join(sorted(word))
            anagram_grouped[sorted_word].append(word)
        
        # Return the grouped list
        return list(anagram_grouped.values())
        
            


            











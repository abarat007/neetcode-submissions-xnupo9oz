class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {} # letter: [greater_than_letter]

        N = len(words)

        for word in words:
            for char in word:
                if char not in adj:
                    adj[char] = []

        for i in range(1, N):
            prev_word = words[i-1]
            curr_word = words[i]

            if len(prev_word) > len(curr_word) and prev_word.startswith(curr_word):
                return ""
            
            traversed_length = min(len(prev_word), len(curr_word))
            for j in range(traversed_length):
                if prev_word[j] != curr_word[j]:
                    if curr_word[j] not in adj[prev_word[j]]:
                        adj[prev_word[j]].append(curr_word[j])
                    break
                    
        
        visited = set()
        visiting = set()
        res = []

        def dfs(letter):
            if letter in visiting:
                return False
            if letter in visited:
                return True
            
            visiting.add(letter)

            for char in adj[letter]:
                if not dfs(char):
                    return False
            
            visiting.remove(letter)
            visited.add(letter)
            res.append(letter)
            return True
            

        for letter in adj:
            if not dfs(letter):
                return ""
        
        return "".join(res[::-1])

        # 'n': ['f'] 
        # 'h': ['e'] 
        # 'r': ['n'] 
        # 'e': ['r']

        



        
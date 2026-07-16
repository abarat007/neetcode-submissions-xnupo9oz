class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # make dict {char: idx} for words
        order_dict = {ch : i for i, ch in enumerate(order)}

        # compare adjacent words as you loop through words
        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]
            for j in range(len(word1)):
                # If i am still iterating through word 1 and word 2 is gone,
                # that means that word 2 is a prefix of word 1, and it should be before word1
                # therefore, return false
                if j == len(word2):
                    return False
                # if the letter in the second word has a lower index value
                # than the letter in the first word, return false
                if word1[j] != word2[j]:
                    if order_dict[word1[j]] > order_dict[word2[j]]:
                        return False
                    break
        return True




        
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        
        existing_word1 = {}
        existing_word2 = {}
        for char in set(word2):
            existing_word2[char] = word2.count(char)

        for char in set(word1):
            existing_word1[char] = word1.count(char)

        if sorted(existing_word1.keys()) != sorted(existing_word2.keys()):
            return False

        if sorted(existing_word1.values()) != sorted(existing_word2.values()):
            return False            

        return True
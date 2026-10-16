class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        output = ""

        for a,b in zip(word1, word2):
            output += a + b

        n = min(len(word1), len(word2))

        return output + word1[n:] + word2[n:]
        
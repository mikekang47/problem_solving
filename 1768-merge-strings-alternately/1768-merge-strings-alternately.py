class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str: 
        s = ""
        for i,j in zip(list(word1), list(word2)):
            s += i
            s += j
        if len(word1) > len(word2):
            s += word1[len(word2):]
        else:
            s += word2[len(word1):]
        return s

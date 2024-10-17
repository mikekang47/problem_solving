from itertools import combinations

class Solution:
    def letterCombinations(self, digits: str):
        if len(digits) < 1:
            return []
        dic = {"2": "abc", "3": "def", "4":"ghi","5":"jkl", "6":"mno", "7": "pqrs", "8":"tuv", "9":"wxyz"}
        arr = []
        for i in list(digits):
            arr.append(list(dic[i]))
        
        return [''.join(combination) for combination in itertools.product(*arr)]

class Solution:
    def removeStars(self, s: str) -> str:
        arr = []
        for i in range(len(s)):
            if len(arr) == 0:
                arr.append(s[i])
            else:
                if s[i] == '*':
                    arr.pop()
                else:
                    arr.append(s[i])
        return ''.join(arr)
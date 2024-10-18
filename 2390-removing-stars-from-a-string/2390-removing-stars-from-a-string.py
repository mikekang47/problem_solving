class Solution:
    def removeStars(self, s: str) -> str:
        stack = []

        for alphabet in s:
            if alphabet == '*':
                stack.pop()
            else:
                stack.append(alphabet)
        
        return "".join(stack)
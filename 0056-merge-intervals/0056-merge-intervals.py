from collections import deque

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        stack = deque(sorted(intervals, key=lambda x: x[0]))
        head = stack.popleft()
        result = []
        while len(stack) != 0:
            poped = stack.popleft()
            if self.canMerge(head, poped):
                temp = self.mergeTwoInterval(head, poped)
                head = temp; 
            else:
                result.append(head)
                head = poped
        result.append(head)
        return result 
            

    
    def mergeTwoInterval(self, i1, i2: List[int]):
        if i1[1] >= i2[1]:
            return i1
        else: 
            return [i1[0],  i2[1]]

    def canMerge(self, i1, i2: List[int]):
        if i1[1]  >= i2[0]:
            return True
        return False
            
        
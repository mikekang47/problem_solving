import sys
from collections import deque

input = sys.stdin.readline

class Stack:
    def __init__(self):
        self.memory = deque()

    def push(self, object):
        self.memory.append(object)

    def pop(self):
        if len(self.memory) == 0:
            return -1
        return self.memory.pop()
    
    def size(self):
        return len(self.memory)
    
    def empty(self):
        return 1 if len(self.memory) == 0 else 0
    
    def top(self):
        return self.memory[len(self.memory)-1] if self.empty() == 0 else -1


def rightBracket(arr):
    stack = Stack()
    for i in arr:
        if i == '(':
            stack.push(i)
        elif i == ')':
            if stack.top() == '(':
                stack.pop()
            else:
                stack.push(i)
    
    if stack.empty() == 1:
        return True 
    else:
        return False

    
n = int(input())
for i in range(n):
    s = input().rstrip()
    result = rightBracket(list(s))
    if result:
        print("YES")
    else:
        print("NO")

import sys
class Stack:
    commandPush = "push"
    commandPop = "pop"
    commandSize = "size"
    commandEmpty = "empty"
    commandTop = "top"

    def __init__(self):
        self.memory = []

    def push(self, num):
        self.memory.append(num)

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


stack = Stack()
n = int(sys.stdin.readline())

for i in range(n):
    line = sys.stdin.readline().split()
    command = line[0] 

    if command == Stack.commandPush:
        num = line[1]
        stack.push(num)
    if command == Stack.commandPop:
        print(stack.pop())
    if command == Stack.commandSize:
        print(stack.size()) 
    if command == Stack.commandEmpty:
        print(stack.empty())
    if command == Stack.commandTop:
        print(stack.top())
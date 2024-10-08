import sys
from collections import deque

class Queue:
    commandPush = "push"
    commandPop = "pop"
    commandSize = "size"
    commandEmpty = "empty"
    commandFront = "front"
    commandBack = "back"

    def __init__(self):
        self.memory = deque()

    def push(self, num):
        self.memory.append(num)

    def pop(self):
        if len(self.memory) == 0:
            return -1
        return self.memory.popleft()
    
    def size(self):
        return len(self.memory)
    
    def empty(self):
        return 1 if len(self.memory) == 0 else 0
    
    def back(self):
        return self.memory[len(self.memory)-1] if self.empty() == 0 else -1
    
    def front(self):
        return self.memory[0] if self.empty() == 0 else -1


queue = Queue()
n = int(sys.stdin.readline())

for i in range(n):
    line = sys.stdin.readline().split()
    command = line[0] 

    if command == Queue.commandPush:
        num = line[1]
        queue.push(num)
    if command == Queue.commandPop:
        print(queue.pop())
    if command == Queue.commandSize:
        print(queue.size()) 
    if command == Queue.commandEmpty:
        print(queue.empty())
    if command == Queue.commandBack:
        print(queue.back())
    if command == Queue.commandFront:
        print(queue.front())
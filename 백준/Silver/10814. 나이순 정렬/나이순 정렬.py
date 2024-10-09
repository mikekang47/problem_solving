import sys
from collections import deque

input = sys.stdin.readline


n = int(input())
class Person:
    def __init__(self, age, name, index):
        self.age = age
        self.name = name
        self.index = index

    
people = []
for i in range(n):
    age, name = input().split()
    people.append(Person(int(age), name, i)) 

people.sort(key=lambda x: (x.age, x.index))

for i in people:
    print(i.age, i.name)
import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())

d = deque()
for i in range(1, n+1):
    d.append(i)

arr = []
while len(d) != 0:
    for i in range(k-1):
      num = d.popleft()
      d.append(num)
    arr.append(d.popleft())


s = "<"
for i in range(len(arr)):
  if i == len(arr) - 1:
    s += str(arr[i]) + '>'
  else:
    s += str(arr[i]) + ', '

print(s)

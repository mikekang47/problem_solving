import sys

input = sys.stdin.readline

n = int(input().rstrip())

arr = []
for i in range(n):
    word = input().rstrip()
    arr.append(word)

arr = list(set(arr))

arr.sort(key=lambda x: (len(x), x))

for i in arr:
    print(i)

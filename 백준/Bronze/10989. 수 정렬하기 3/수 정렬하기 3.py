import sys

input = sys.stdin.readline


n = int(input())
arr = [0] * 10001

for i in range(n):
    n = int(input())
    arr[n] += 1

for i in range(len(arr)):
    if arr[i] != 0:
        for j in range(arr[i]):
            print(i)

import sys

input = sys.stdin.readline

n =  int(input())

num = 666

arr = []
while len(arr) != n:
    if str(num).find('666') != -1:
      arr.append(num)
    num += 1


print(arr[n-1])  
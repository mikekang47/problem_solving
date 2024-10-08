import sys
from collections import defaultdict

input = sys.stdin.readline

n = int(input().rstrip())
arr1 = list(map(int, input().rstrip().split()))
m = int(input().rstrip())
arr2 = list(map(int, input().rstrip().split()))

dic = defaultdict(int)
for i in arr1:
    dic[i] += 1

for i in arr2:
    if dic[i] != 0:
        print(1)
    else:
        print(0)
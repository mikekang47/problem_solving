import sys

input = sys.stdin.readline


n = int(input())
subjects = list(map(int, input().split()))

def newPoint(high, point):
    return point / high * 100

highPoint = max(subjects)
for i in range(len(subjects)): 
     subjects[i] = newPoint(highPoint, subjects[i])

print(sum(subjects) / len(subjects))
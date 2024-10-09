import sys
import math
from collections import defaultdict

input = sys.stdin.readline

n = int(input().rstrip())

def isPrime(n):
    if n == 1:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    
    return True

arr = list(map(int, input().rstrip().split()))
cnt = 0
for i in arr:
    if isPrime(i):
        cnt += 1
print(cnt)

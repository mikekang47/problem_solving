import sys
import math

input = sys.stdin.readline


def isPrime(n):
    if n == 1:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    
    return True

m, n = map(int, input().rstrip().split())
for i in range(m, n+1):
    if isPrime(i):
        print(i)

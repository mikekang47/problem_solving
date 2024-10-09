import sys
from collections import defaultdict

input = sys.stdin.readline

n = int(input().rstrip())
shirts = list(map(int, input().rstrip().split()))
t, p = map(int, input().rstrip().split())

bundle = 0
for shirt in shirts:
    portion = shirt // t
    rest = shirt % t
    if rest == 0:
        bundle += portion
    else:
        bundle += portion + 1


bunch = n // p
rest = n % p

print(bundle)
print(bunch, rest)
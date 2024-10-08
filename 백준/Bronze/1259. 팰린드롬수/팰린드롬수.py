import sys

input = sys.stdin.readline

while True:
    s = input().rstrip()
    if s == '0':
        exit(0)
    reverse = ''.join(s[::-1])
    if reverse == s:
        print("yes")
    else:
        print("no")
 
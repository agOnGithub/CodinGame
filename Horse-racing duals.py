import sys

n = int(input())
l = []
for i in range(n):
    l.append(int(input()))
l.sort()

d = sys.maxsize
for i in range(1, n):
    d = min(d, l[i] - l[i - 1])

print(d)
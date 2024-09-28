import sys
import math

n = int(input())  # the number of temperatures to analyse
temps = []
closest = 0
if n == 0: print(0)
else:
    for i in input().split():
        temps.append(int(i))
    closest = min(temps, key=abs)

    if -closest in temps and -closest > 0:
        closest = -closest

    print(closest)
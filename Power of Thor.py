import sys
import math

light_x, light_y, initial_tx, initial_ty = [int(i) for i in input().split()]
thor_x, thor_y = initial_tx, initial_ty

while True:
    remaining_turns = int(input())  # The remaining amount of turns Thor can move. Do not remove this line.
   
    d_x, d_y = "", ""
    if light_x < thor_x:
        d_x += "W"
        thor_x -= 1
    elif light_x > thor_x:
        d_x += "E"
        thor_x += 1

    if light_y < thor_y:
        d_y += "N"
        thor_y -= 1
    elif light_y > thor_y:
        d_y += "S" 
        thor_y += 1
    print(d_y + d_x)
import sys
import math

l = int(input()) #width of the letter
h = int(input()) #height of the letter
t = input().upper() #stuff to print out
for i in range(h):
    row = input() #ready made line of ascii alphabet

    for j in range(len(t)):
        #Get ASCII index of current char.
        char = ord(t[j]) - ord('A')
        letter = char if t[j].isalpha() else ord('Z') - ord('A') + 1
        
        #Get ASCII line of current char.
        ascii = row[letter * l : (letter + 1) * l]
        
        #Print ASCII line part.
        print(ascii, end='')
    
    print()
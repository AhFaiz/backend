from array import *

print("=== PROGRAM 1 ===")

T = [[11,12, 5, 2], 
     [15, 6, 10], 
     [10, 8, 12, 5], 
     [12,15, 8, 6]]

print(T[0])

print(T[1][2])


print("\n=== PROGRAM 2 ===")
T = [[11, 12, 13, 14], [15, 16,17], [18, 19, 20, 21], [22, 23, 24,25]]
for r in T:
   for c in r:
      print(c,end = " ")
   print()
   
   
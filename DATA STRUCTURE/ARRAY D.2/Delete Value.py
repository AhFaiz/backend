from array import *

print("=== PROGRAM MATRIX 1 ===")
T = [[11, 12, 5, 2], [15, 6,10], [10, 8, 12, 5], [12,15,8,6]]

#Delete Value
del T[3]

for r in T:
   for c in r:
      print(c,end = " ")
   print()
   
   
print("\n=== PROGRAM MATRIX 2 ===")
R = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 11, 11, 12], [13,14]]

del R[3]

for x in R:
    for z in x:
        print(z, end = " ")
    print()

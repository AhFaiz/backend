from array import *

print("=== PROGRAM MATRIX 1 ===")
T = [[11, 12, 5, 2], [15, 6, 10], [10, 8, 12, 5], [12, 15, 8, 6]]

T.insert(2, [0,5,11,13])

for r in T:
    for x in r:
        print(x,end = " ")
    print()
    
#========================================
    
print("\n=== PROGRAM MATRIX 2 ===")

MATRIX = [[11, 12, 13, 14], [19, 20, 21], [22, 23, 24, 25]]

MATRIX.insert (1, [15, 16, 17, 18])

for a in MATRIX:
    for b in a:
        print(b,end = " ")
    print()

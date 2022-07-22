from array import *

print("=== PROGRAM MATRIX 1 ===")
T = [[11, 12, 5, 2], [15, 6,10], [10, 8, 12, 5], [12,15,8,6]]

#insert :
#Mengubah Nilai Keseluruhan
T[2] = [11,9]

#Mengubah Value
T[0][3] = 7

#Membentuk MATRIX
for r in T:
   for c in r:
      print(c,end = " ")
   print()



print("\n=== PROGRAM MATRIX 2 ===")
R = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 11, 11, 12], [13,14]]

#Insert
R[3] = [13, 14, 15, 16]
R[2][1] = 10 

#Membentuk MAtrix
for x in R:
    for z in x:
        print(z,end = " ")
    print()

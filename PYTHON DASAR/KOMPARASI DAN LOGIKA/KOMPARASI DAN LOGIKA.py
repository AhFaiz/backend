#Be;ajar Komparasi dan Logika

#Membuat Area rentang dari angka

#++++++++3-------10++++++#
print("MASUKKAN ANGKA <3 atau >10")
User = float(input("Masukkan angka : "))

#Rumus <3
Kurang_dari_3 = (User <3)
print ("kurang dari 3 = ", Kurang_dari_3) 

#Rumus >10
Lebih_dari_10 = (User >10)
print ("Lebih dari 10 = ", Lebih_dari_10)

#Logika
Correct = Kurang_dari_3 or Lebih_dari_10
print ("Angka yang anda masukkan adalah = ", Correct)

print("\n=========================\n")

#-------3+++++++10-------#
print ("Masukkan angka >3 dan <10")
User = float(input("Masukkan angka : "))

#Rumus >3
Lebih_dari_3 = (User >3)
print ("Lebih dari 3 = ", Lebih_dari_3)

#Rumus <10
Kurang_dari_10 = (User <10)
print ("Kurang dari 10 = ", Kurang_dari_10)

#Logika
Correct = Lebih_dari_3 and Kurang_dari_10
print ("Angka yang anda masukkan adalah = ", Correct)

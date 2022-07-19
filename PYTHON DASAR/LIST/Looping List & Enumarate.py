class SATU:
    def __init__ (self):
        print(" ==== 1. FOR LOOP ====")
        
belajar = SATU()

#======================================#

print("\n--- CONTOH 1 ---")

angka = [4,3,2,5,6,1]

for angka in angka:
	print(f"angka = {angka}")

#======================================#
print("\n--- CONTOH 2 ---")

peserta = ["neuvill","pace","jupri","wisnu","randi"]

for nama in peserta:
	print(f"nama = {nama}")

#--------------------------------------#
class DUA :
    def __init__ (self):
        print("\n ==== 2. FOR LOOP AND RANGE")
        
belajar = DUA()

#======================================#
print("\n--- CONTOH 1 ---")

angka = [10,5,4,2,6,5]

panjang = len(angka)

for i in range(panjang):
	print(f"angka = {angka[i]}")
 

#---------------------------------------#
class TIGA :
    def __init__(self):
        print("\n ==== 3. WHILE LOOP ====")
        
belajar = TIGA()

#===================================#
print("\n--- CONTOH 1 ---")
kumpulan_angka = [10,5,4,2,6,5]

panjang = len(kumpulan_angka)
i = 0

while i < panjang:
	print(f"angka = {kumpulan_angka[i]}")
	i += 1

#--------------------------------------------------#
class EMPAT :
    def __init__(self):
        print("\n ==== 4. LIST COMPREHENTION ====")
        
belajar = EMPAT()

#==================================#
print("\n--- CONTOH 1 ---")

data = ["ucup",1,2,3,"otong"]

[print(f"data={i}") for i in data]

angka = [10,5,4,2,6,5]

angka_kuadrat = [i**2 for i in angka]
print(angka_kuadrat)

#------------------------------------------------#
class LIMA:
    def __init__ (self):
        print ("\n ==== 5. ENUMERATE ====")

belajar = LIMA()

#======================================#
print("\n--- CONTOH 1 ---")
data_list = ["ucup",1,2,3,"otong"]

for index,data in enumerate(data_list):
	print(f"index = {index}, data = {data}")
class CALCULATOR :
    def __init__ (self):
        print("=== HI CALCULATOR ===\n")

calculator = CALCULATOR ()

def tambah(x, y): #untuk pertambahan
    return x + y
 
def kurang(x, y): #untuk pengurangan
    return x - y
 
def kali(x, y): #untuk perkalian
    return x * y
 
def bagi(x, y): #untuk pembagian
    return x / y

#Menunjuka user operasi yang ada 
print('Menu Operasi:\n1. Penjumlahan\n2. Pengurangan\n3. Perkalian\n4. Pembagian')

#mengulang program dari awal
ulang = 'y'
while ulang == 'y' :
    
    #menginput opeasi apa yang user mau dengan angka
    operasi = int(input('silahkan masukan operasi pilihan (dalam angka): '))
    x = int(input('masukan angka1   : '))
    y = int(input('masukan angka2   : '))

    #statement  jika user memeilih penjumlahan
    if operasi == 1:
        print("Hasil :" ,tambah(x, y))
    
    #statement jika user memilih pengurangan            
    elif operasi == 2:
        print("Hasil :" ,kurang(x, y))
    
    #statement jika user memilih perkalian   
    elif operasi == 3:
        print("Hasil :" ,kali(x, y))
          
    #statement jika user memilih pembagian      
    elif operasi == 4:
        print("Hasil :" ,bagi(x, y))
    

    ulang = (input("Mau Ngulang? (y/t) : "))
    if ulang == 't':
        print("\n=== THANK YOU ===")

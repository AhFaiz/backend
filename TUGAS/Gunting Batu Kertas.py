class GBK:
  def __init__ (self):
    print(" Gunting Batu Kertas ")
    
game = GBK()

#========== PROGRAM ==========
from random import randint

#set untuk mengulang ke awal game
ulang = "y"
while ulang.lower() == "y":
  
    #membuat list option 
    list = ["gunting", "batu", "kertas"]
    
    #memanggil variable list untuk dijadikan pilihan komputer
    komputer = list[randint(0,2)]
    
    #tampilan awal
    print(">"*35)
    print("--- Permainan Dimulai ---")
    print("<"*35,"\n")
    
    #set pemain/user
    pemain = input("Masukkan pilihan Gunting, Batu, Kertas ? : ")
    
    #set jika pemain sama dengan komputer
    if pemain.lower() == komputer:
      print()
      print("="*20)
      print("Kamu = ",pemain, "\nKomputer =", komputer)
      print("Hasil suit Seri!")
      print("="*20,"\n")
      
    #set jika pemain memilih gunting
    elif pemain.lower() == "gunting":
        
        #set jika komputer batu 
        if komputer == "batu":
          print()
          print("="*20)
          print("Hasil Suit Kalah :(")
          print("Kamu     =", pemain, "\nKomputer =", komputer)
          print("="*20,"\n")
        
        #set jika komputer kertas
        else:
          print()
          print("="*20)
          print("Kamu Menangg :)")
          print("Kamu     =", pemain, "\nKomputer = ", komputer)
          print("="*20,"\n")
    
    #set jika pemain memilih batu      
    elif pemain.lower() == "batu":
        
        #set jika komputer memilih kertas
        if komputer == "kertas":
          print()
          print("="*20)
          print("Yahh kamu kalah :(")
          print("Kamu      =", pemain, "\nKomputer = ", komputer)
          print("="*20,"\n")
        
        #set jika komputer memilih gunting
        else:
          print()
          print("="*20)
          print("Kamu Menangg :)")
          print("Kamu     =", pemain, "\nKomputer = ", komputer)
          print("="*20,"\n")
    
    #set jika pemain memilih kertas
    elif pemain.lower() == "kertas":
        
        #set jika komputer memilih komputer
        if komputer == "gunting":
          print()
          print("="*20)
          print("Yahh kamu kalah :(")
          print("Kamu     =", pemain, "\nKomputer = ", komputer)
          print("="*20,"\n")
        
        #set jika komputer memilih batu
        else:
          print()
          print("="*20)
          print("Kamu Menangg :)")
          print("Kamu     =", pemain, "\nKomputer = ", komputer)
          print("="*20,"\n")
    
    #set jika pemain tidak memilih opsi yang ada
    else:
        print("Pilihan yang kamu masukan salah...")
    
    #set untuk mengulang permainan ke awal   
    ulang = input("Apakah kamu ingin bermain kembali? Y/N = ")
    
    #set jika pemain memilih 'N'
    if ulang == 'N':
      print(">>> Have A Good Day :) <<<")
#BENTUK 1

class PROGRAMMER:
    pass

Pace    = PROGRAMMER()
Randi   = PROGRAMMER()

Pace.PROGRAMMER   = "Paang"
Randi.PROGRAMMER  = "Randi"

print("==== Programmer ====")
print(Pace.PROGRAMMER)
print(Randi.PROGRAMMER)

class UI:
    pass

Nepil   = UI()
Ferdy   = UI()

#Pace adalah objek dari sebuah class user yang nilai atributnya programer nya adalah Pace
Nepil.UI    = "Neuvill"
Ferdy.UI   = "Coon"

print("\n====UI====")
print(Nepil.UI)
print(Ferdy.UI)

#BENTUK 2

class Gaamon:
    def __init__(self):
        print("JUPRI KEMBUR")
        
Pace    = Gaamon()
Randi   = Gaamon()

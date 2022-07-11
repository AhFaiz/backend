class TRY :
    def __init__ (self):
        print("=== Latihan Property ===")

belajar = TRY ()

class PROPERTY1 :
    def __init__ (self, name, role, lane):
        self.name = name
        self.__role = role
        self.lane = lane
    
    def AllInfo (self):
        return F"{self.name} {self.__role} {self.lane} is ready"
    
    def update_role(self, new_role):
        if self.__role != "Tank":
            self.__role = new_role
            
    def UnPrivRole (self):
        return self.__role
    
heroes = PROPERTY1 ("Hylos", "Tank", "MidLane")

#-------- BENTUK 1 Tidak Menggunakan Decorator PROPERTY ---------
print("\n----- Bentuk 1 Tanpa Decorator Property -----\n")
print(heroes.AllInfo())

#ubah nama
print("Update Name")
heroes.name = "Karrie"
print("- Name    : ",heroes.name)
print("- Updated : ",heroes.AllInfo())

#ubah role
print("Ubah Role")
heroes.__role = "MM"
print("- Role    : ",heroes.__role)
print("- Updated : ",heroes.AllInfo())

#ubah lane
print("Ubah Lane")
heroes.lane = "GoldLane"
print("- Lane    : ",heroes.lane)
print("- Updated : ",heroes.AllInfo())

#==========================================================#
print("\n----- Bentuk 2 Dengan Decorator Property -----\n")

class PROPERTY2 :
    def __init__ (self, name, role, lane):
        self.name = name
        self.__role = role
        self.lane = lane
        
    def AllInfo(self):
        return f"{self.name} {self.__role} {self.lane} is good"

    @property #berguna untuk memanggil role dengan syntax role biasa bukan __role
    def UnPrivRole(self):
        return self.__role
    
    @UnPrivRole.setter #digunakan disaat memasukkan nilai menggunakan = bukan ()
    def role(self, new_role):
        if self.__role != "Tank" :
            self.__role = new_role
            
#-------- BENTUK 2 Menggunakan Decorator PROPERTY ---------

print("\n>>>>> CONTOH 1 <<<<<\n")

heroes = PROPERTY2 ("Hylos", "Tank", "MidLaner")
print(heroes.AllInfo())

#ubah nama
print("Update Name")
heroes.name = "Karina"
print("- Name    : ",heroes.name)
print("- Updated : ",heroes.AllInfo())

#ubah role
print("Update Role")
heroes.role = "Magic"
print("- Role    : ",heroes.role)
print("- Updated : ",heroes.AllInfo())

#ubah lane
print("Update Lane")
heroes.lane = "GoldLane"
print("- Lane    : ",heroes.lane)
print("- Updated : ",heroes.AllInfo())

print("\n<<<<< CONTOH 2 >>>>>\n")

heroes2 = PROPERTY2 ("Karina", "Magic", "Hyper")
print(heroes2.AllInfo())

#ubah nama
print("Update Name")
heroes2.name = "Beatrix"
print("- Name    : ",heroes2.name)
print("- Updated : ",heroes.AllInfo())

#ubah role
print("Update Role")
heroes2.role = "Marksman"
print("- Role    : ",heroes2.role)
print("- Updated : ",heroes2.AllInfo())

#ubah lane
print("Update Lane")
heroes2.lane = "GoldLane"
print("- Lane    : ",heroes2.lane)
print("- Updated : ",heroes2.AllInfo())







            
    
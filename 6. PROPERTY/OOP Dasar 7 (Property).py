print("\n<<<<< BENTUK 1 >>>>>")

class PROGRAMER :
    def __init__  (self, name, gmail, role):
        self.name   = name
        self.gmail  = gmail
        self.__role = role
        
    def info (self):
        return f"{self.name} - {self.gmail} - {self.__role}"
    
    def update_role(self, new_role):
        if self.__role != "FrontEnd":
            self.__role = new_role
    
    @property     
    def role(self):
        return self.__role
            
    
Pace = PROGRAMER ("Pace", "Pace@gmail.com", "FrontEnd")

#BENTUK 1
Pace.__role = "UI UX"
print(Pace.__role)
print(Pace.info())
print("Hasil Akhir = " , Pace.role)
print(">> UI UX Gamasuk Ke Dalam Function Info\n")

#BENTUK 2
Pace._PROGRAMER__role = "UI UX"
print(Pace._PROGRAMER__role)
print(Pace.info())
print("Hasil Akhir = ", Pace.role)
print(">> UI UX Masuk Ke dalam Function Info\n ")

Pace.name   = "Paangggg"
print(Pace.name)
print(Pace.info())
#CATATAN:
#- kalo mau pake print(pace.role()', @property -nya harus diilangin dulu

print("\n ==== Bentuk 2 Aturan Logic Role FrontEnd ====")

class PROGRAMER :
    def __init__  (self, name, gmail, role):
        self.name   = name
        self.gmail  = gmail
        self.__role   = role
        
    def info (self):
        return f"{self.name} - {self.gmail} - {self.__role}"
    
    @property
    def role(self):
        return self.__role
    
    @role.setter
    def role(self, new_role):
        if self.__role != "FrontEnd":
            self.__role = new_role
            
    
Pace    = PROGRAMER ("Pace", "Pace@gmail.com", "FrontEnd")
Nepil   = PROGRAMER ("Wisnu", "Randi@gmail.com", "UI")

Pace.role   = "JOKI ILAB"
print(Pace.info())

Nepil.role  = " UI WEB & ANDROID "
print(Nepil.info())

print(Pace.role)


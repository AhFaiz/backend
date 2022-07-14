class PROGRAMER :
    def __init__  (self, name, gmail, role):
        self.name   = name
        self.gmail  = gmail
        self.__role   = role
        
    def info (self):
        return f"{self.name} - {self.gmail} - {self.__role}"
    
    def update_role(self, new_role):
        if self.__role != "FrontEnd":
            self.__role = new_role
    
    #function baru (biar garibet) buat manggil role   
    def RoleLama (self):
        return self.__role
    
randi = PROGRAMER ("Randi Irwansyah", "Randi@gmail.com", "FrontEnd")
print(randi.__dict__)
print("\n==== Data Awal ====")
print(randi.info())
print("Role Awal    : ",randi._PROGRAMER__role)


#menggunakan bypass
print("\n==== Ubah Role dengan Cara ByPass ====")
randi._PROGRAMER__role = "Joki Ilab"
print(randi.info())
print("Role Updated : ",randi._PROGRAMER__role)

#Biar Enak manggil Role
print ("\n <<<< Bentuk Baru >>>> ")
print(randi.RoleLama())


 
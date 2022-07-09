#BENTUK 1
print("---- Bentuk Pertama ----")    

class EXSYNC :
    def __init__ (self, name, gmail, role):
        self.name   = name
        self.gmail  = gmail
        self.role   = role
    
    def work(self):
        return f"{self.name} {self.role} is working"

randi = EXSYNC ("Randi", "randi@gmail.com", "FrontEnd")
print("-",randi.work())

#BENTUK 2 (INHERITANCE)
print("\n---- Bentuk 2 ----")

class EXSYNC:
    def __init__ (self, name, gmail, role):
        self.name   = name
        self.gmail  = gmail
        self.role   = role
        
    def coding(self):
        return f"{self.name} {self.gmail} {self.role} is available"
    
#INHERITANCE
class PROGRAMER (EXSYNC):
    def __init__ (self, name, gmail, role, level):
        super(). __init__ (name, gmail, role)
        self.level = level
     
    #override / menimpa   
    def work(self):
       return f"{self.name} {self.gmail} {self.role} {self.level} is writing code"
    
    #extend
    def debug (self):
        return "is debugging"
    

pace = EXSYNC ("Pace", "pace@gmail.com", "FrontEnd")
print(pace.coding())

jupri = PROGRAMER ("Adrian", "Adrian@gmail.com", "FullStack", "Profesional")
print(jupri.work())

print("Jupri",jupri.debug())

#jadi INHERITANCE berguna untuk mewarisi dari constructor init dan 
# juga method dari class EXSYNC





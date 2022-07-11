class TRY :
    def __init__ (self):
        print("=== Latihan Constructor ===")
        
constructor = TRY ()

class CEO:
    def __init__ (self, name, age, role):
        self.name   = name
        self.age  = age
        self.role   = role
        
    def InfoFS(self):
        return f"{self.name} is available"
    
    def Biodata(self):
        return f"Biodata FullStack :  {self.name} - {self.age} - {self.role}"

fullstack = CEO ("Adrian", "Adrian@gmail.com", "FullStack")

print("\n--- CEO --- ")
print(fullstack.Biodata())
print(fullstack.InfoFS())    

class BACKEND :
    def __init__ (self, name, gmail, role):
        self.name   = name
        self.gmail  = gmail
        self.role   = role
        
    def InfoBE (self):
        return f"{self.name} {self.role} is available"
    
    def Biodata (self):
        return f"Biodata BackEnd : {self.name} - {self.gmail} - {self.role}"
    
backend = BACKEND ("Faiz", "Faiz@gmail.com", "BackEnd")

print("\n--- Welcome to BackEnd --- ")
print(backend.Biodata())
print(backend.InfoBE())

class FRONTEND :
    def __init__ (self, name, gmail, role):
        self.name   = name
        self.gmail  = gmail
        self.role   = role
        
    def InfoFE (self):
        return f"{self.name} {self.role} is available"
    
    def Biodata (self):
        return f"Biodata FrontEnd :{self.name} - {self.gmail} - {self.role}"
    
frontend1 = FRONTEND ("Pace", "Pace@gmail.com", "FrontEnd")
frontend2 = FRONTEND ("Randi", "Randi@gmail.com", "FrontEnd")

print("\n--- Welcome to FrontEnd ---")

print(frontend1.Biodata())
print(frontend2.Biodata())

print(frontend1.InfoFE())
print(frontend2.InfoFE())

class UIUX :
    def __init__ (self, name, gmail, role):
        self.name   = name
        self.gmail  = gmail
        self.role   = role 
        
    def InfoUIUX (self):
        return f"{self.name} {self.role} is available"
    
    def Biodata (self):
        return f"{self.name} - {self.gmail} - {self.role}"
    

uiux1 = UIUX ("Neuvill", "Neuvill@gmail.com", "UIUX")
uiux2 = UIUX ("Ferdy", "Ferdy@gmail.com", "UIUX")

print("\n--- Welcome to UIUX ---")

print(uiux1.Biodata())
print(uiux1.InfoUIUX())

print(uiux2.Biodata())
print(uiux2.InfoUIUX())

class DigCreat:
    def __init__ (self, name, gmail, role):
        self.name   = name
        self.gmail  = gmail
        self.role   = role

    def Biodata (self):
        return f"{self.name} - {self.gmail} - {self.role}"
    
    def InfoDC (self):
        return f"{self.name} {self.role} is available"
    
DigCreat1 = DigCreat ("Rehan", "Rehan@gmail.com", "Digital Creator")
DigCreat2 = DigCreat ("Fido", "Fido@gmail.com", "Digital Creator")

print("\n--- Welcome to Digital Creator ---")

print(DigCreat1.Biodata())
print(DigCreat1.InfoDC())

print(DigCreat1.Biodata())
print(DigCreat2.InfoDC())

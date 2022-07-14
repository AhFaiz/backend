print("==== Class Variabel ====")

class Programer:
    total1 = 0
    
    def __init__(self, name, email, role):
        self.name = name
        self.email = email
        self.role = role
        Programer.total1 += 1
        
Pace    = Programer("Paang", "paang@gmail.com", "FronteND")
print("==== Programmer 1 ====")
print(Pace.name)
print(Pace.email)
print(Pace.role)
print(Programer.total1)


Randi   = Programer("Randi", "randi@gmail.com", "UX" )
print("\n=== Programmer 2 ====")
print(Randi.name)
print(Randi.email)
print(Randi.role)
print(Programer.total1)


Jupri   = Programer("Jupri", "Jupri@gmail.com", "BackEnd")
print("\n=== Programmer 3 ====")
print(Randi.name)
print(Randi.email)
print(Randi.role)
print(Programer.total1)

class UI:
    total2 = 0
    
    def __init__(self,name,email,role):
        self.name   = name
        self.email  = email
        self.role   = role
        UI.total2 += 1
        
Nepil = UI("Neuvill Ikhwan Danuarta", "Neuvill@gmail.com", "UI")
print("\n==== UI 1 ====")
print(Nepil.name)
print(Nepil.email)
print(Nepil.role)
print(UI.total2)

Ferdy = UI("Ferdy", "Ferdy@gmail.com", "UI")
print("\n==== UI 2 ====")
print(Ferdy.name)
print(Ferdy.email)
print(Ferdy.role)
        

        


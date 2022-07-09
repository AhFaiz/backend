print("==== EXSYNC DEV ====")


class Programer:
    def __init__(self, name, email, role):
        self.name   = name
        self.email  = email
        self.role   = role
        
Pace    = Programer("Paang", "paang@gmail.com", "FrontEnd")

print("==== Programmer 1 ====")
print(Pace.name)
print(Pace.email)
print(Pace.role)

Randi   = Programer("Randi", "randi@gmail.com", "UX" )

print("\n=== Programmer 2 ====")
print(Randi.name)
print(Randi.email)
print(Randi.role)

class UI:
    def __init__(self,name, email, role):
        self.name   = name
        self.email  = email
        self.role   = role
        
Nepil = UI("Neuvill", "Neuvill@gmail.com", "UI")
Ferdy = UI("Ferdy", "Ferdy@gmail.com", "UI")


print("\n==== UI 1 ====")
print(Nepil.name)
print(Nepil.email)
print(Nepil.role)

print("\n==== UI 2 ====")
print(Ferdy.name)
print(Ferdy.email)
print(Ferdy.role)




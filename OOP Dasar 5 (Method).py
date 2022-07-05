
print(">>>>> PERTEMUAN 5 METHOD <<<<<")

class PROGRAMER:
    #method 1
    def __init__(self, name, email, role):
        self.name   = name
        self.email  = email
        self.role   = role
    
    #method 2
    def update_name(self, new_name):
        self.name = new_name
    
    #method 3
    def update_email(self, new_email):
        self.email = new_email
        
    #method 4   
    def update_role(self, new_role):
        if self.role != "UI":
            self.role = new_role
            
    #method 5
    def info(self):
        return f"{self.name} - {self.email} - {self.role}"
    
blek    = PROGRAMER ("Blek", "Blek@gmail.com", "UI")
jupri   = PROGRAMER ("Jupri", "Jupri@gmail.com", "BackEnd")

#output untuk method 1 blek
print("\n=== Biodata Neuvill ===")
print("-Name        :", blek.name)
print("-Email       :", blek.email)
print("-Role        :", blek.role)

print("\nUpdate Data Neuvill")
#output untuk method 2
blek.update_name("Neuvill")
print("-Update Name     :", blek.name)

#output untuk method 3
blek.update_email("Neuvill@gmail.com")
print("-Update Email    :", blek.email)

#output untuk method 4
blek.update_role("UI WEB & ANDROID")
print("-Update Role     :", blek.role)

#output untuk method 5
print("Data Updated     :", blek.info())

#==========================================================

#output untuk method 1 Jupri
print("\n=== Biodata Jupri ===\n")
print("-Name    :", jupri.name)
print("-Email   :", jupri.email)
print("-Role    :", jupri.role)

print("\nUpdate Data Jupri")

#output untuk method 2
jupri.update_name("Adrian Des")
print("-Update Name     :", jupri.name)

#output untuk method 3
jupri.update_email("Adrian@gmail.com")
print("-Update Email    :", jupri.email)

#output untuk method 4
jupri.update_role("FullStack")
print("-Update Role     :", jupri.role)

#output untuk method 5
print("Data Updated    :", jupri.info())





     


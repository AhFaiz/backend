class EXSYNC:
    def __init__ (self, name, email, role):
        self.name   = name
        self.email  = email
        self.role   = role
        
    def work (self):
        return f"is working"
    
ferdy = EXSYNC ("Ferdy", "Ferdy@gmail.com", "UI")

class Flutter (EXSYNC):
    def __init__ (self, name, email, role, level):
        super(). __init__ (name, email, role)
        self.level = level
    
    def debug(self):
        return "is debugging"
    
    def work (self):
        return f"{self.name} is creating some programs"
    
adam = Flutter ("Adam", "adam@gmail.com", "Flutter", "Expert")

print(adam.work())

class FrontEnd (EXSYNC):
    def __init__ (self, name, email, role, level, APP):
        super(). __init__ (name, email, role)
        self.level  = level
        self.APP    = APP
    
    def debug (self):
        return "not available"
    
    def work (self):
        return f"{self.name} is creating some programs from PHP"
    
pace = FrontEnd ("Pace", "Pace@gmail.com", "FrontEnd", "Expert", "PHP")

print(pace.work())

def working(bebek):
    print("Yang kepanggil = ",bebek.work())

working(ferdy)

print(len("qqwerrty"))



    
print ("---- BENTUK 1 ----")
class EXSYNC:
    def __init__ (self, name, gmail, role):
        self.name   = name
        self.gmail  = gmail
        self.role   = role
    
    def work(self):
        return f"{self.name} is available"

adhit = EXSYNC ("Adhit", "Randi@gmail.com", "FrontEnd")

print(adhit.work())

print("\n---- BENTUK 2 ----")
class PROGRAMER (EXSYNC):
    def __init__ (self, name, email, role, level):
        super().__init__(name, email, role)
        self.level = level
    
    def work(self):
        return f"{self.name} is creating some programs"

    def debug(self):
        return "BREAK CODING"
    
Pace = PROGRAMER ("Pace", "Pace@gmail.com", "FrontEnd", "Profesional")
    
print(Pace.work())

print("\n---- BENTUK 3 ----")
class DESIGNUI (EXSYNC):
    def __init__ (self, name, email, role, level, tools):
        super(). __init__ (name, email, role)
        self.level = level
        self.tools = tools
    
    def debug(self):
        return "BREAK DESIGN"
    
    def work(self):
        return f"{self.name} is creatign some design"
    
Nepil = DESIGNUI ("Nepil", "Nepil@gmail.com", "UI", "Expert", "FIGMA")
    
print(Nepil.work())

        
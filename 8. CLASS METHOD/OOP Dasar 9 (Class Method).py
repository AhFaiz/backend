print("<<<<< Class Method >>>>>")

print("--- Bentuk 1 ---")
class PROGRAMER:
    total = 0
    
    def __init__(self, name, email, role):
        self.name      = name
        self.email     = email
        self.__role    = role
        PROGRAMER.total += 1
        
    def info (self):
        return f"{self.name} - {self.email} - {self.__role}"
    
    @property
    def role (self):
        return self.__role
    
    @role.setter
    def role (self, new_role):
        if self.__role != "UI":
            self.__role = new_role

randi = PROGRAMER ("Randi", "randi@gmail.com", "FrontEnd")

print(PROGRAMER.total)

print("--- Bentuk 2 ---")

class PROGRAMER:
    total = 0
    
    def __init__(self, name, email, role):
        self.name      = name
        self.email     = email
        self.__role    = role
        PROGRAMER.total += 1
        
    def info (self):
        return f"{self.name} - {self.email} - {self.__role}"
    
    @property
    def role (self):
        return self.__role
    
    @role.setter
    def role (self, new_role):
        if self.__role != "DB":
            self.__role = new_role
            
    @classmethod
    def setTotal (cls, total):
        cls.total = total
        
        
randi = PROGRAMER ("Randi", "randi@gmail.com", "FrontEnd")

print(PROGRAMER.total)
PROGRAMER.setTotal(5)
print(PROGRAMER.total)

print("--- Bentuk 3 ---")

class PROGRAMER:
    total = 0
    
    def __init__(self, name, email, role):
        self.name      = name
        self.email     = email
        self.__role    = role
        PROGRAMER.total += 1
        
    def info (self):
        return f"{self.name} - {self.email} - {self.__role}"
    
    @property
    def role (self):
        return self.__role
    
    @role.setter
    def role (self, new_role):
        if self.__role != "DB":
            self.__role = new_role
            
    @classmethod
    def setTotal (cls, total):
        cls.total = total
        
    #classmthod sebagai alternatif 'constructor'
    @classmethod
    def from_string(cls, string_param):
        name, email, role = string_params.split("-")
        return cls (name, email, role)
        
        
randi = PROGRAMER ("Randi", "randi@gmail.com", "FrontEnd")
string_params = "randi-randi@gmail.com-FrontEnd"

sec_randi = PROGRAMER.from_string(string_params)

print(sec_randi.info())







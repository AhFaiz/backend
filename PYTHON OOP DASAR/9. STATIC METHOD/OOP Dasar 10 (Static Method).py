
class PROGRAMER:
    total = 0
    
    def __init__ (self, name, email, role):
        self.name   = name
        self.email  = email
        self.__role = role
        PROGRAMER.total += 1
        
    def info(self):
        return f"{self.name} - {self.email} - {self.__role}"
    
    @property
    def role (self):
        return self.__role
    
    @role.setter
    def role(self, new_role):
        if self.__role != "DB":
            self.__role = new_role
    
    @classmethod
    def setTotal (cls, total):
        cls.total = total
    
    @staticmethod
    def tweet(word):
        return word
    
tweet = PROGRAMER.tweet("HAIII PYTHON")
print(tweet)

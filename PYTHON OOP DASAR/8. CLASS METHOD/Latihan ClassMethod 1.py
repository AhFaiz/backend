
class TRY :
    def __init__ (self):
        print("=== Latihan ClassMethod ===")

latihan = TRY ()

class HEROES :
    total = 0
    
    def __init__ (self, name, role, lane):
        self.name = name
        self.role = role
        self.__lane = lane
        HEROES.total += 1
        
    def AllInfo (self):
        return f"{self.name} {self.role} {self.__lane}"
              
    @property
    def lane (self):
        return self.__lane
    
    @lane.setter
    def lane (self, new_lane):
        if self.__lane != "DB":
            self.__lane = new_lane
            
    @classmethod
    def GetTotal (cls, total):
        cls.total = total
        
    @classmethod
    def NewIns (cls, new_hero):
        name, role, lane = new_hero.split("-")
        return cls (name, role, lane)

print(HEROES.total)

#----INS 1------  
hero = HEROES ("Hylos", "Tank", "MidLane")
print(hero.AllInfo())

#----INS 2------
new_hero = "Beatrix-Marksman-GoldLane"
sec_hero = HEROES.NewIns(new_hero)

print(sec_hero.AllInfo())

print(HEROES.total)


class TRY :
    print("--- Latihan Private Attribute ---")
    
yuk = TRY ()

class HEROES :
    def __init__ (self, name, role, lane):
        self.name   = name
        self.role   = role
        self.__lane = lane
        
    def AllInfo (self):
        return f"{self.name} - {self.role} - {self.__lane}"
    
    #method 3
    def update_lane (self, new_lane):
        if self.__lane != "GoldLaner":
            self.__lane = new_lane
   
    #method 4        
    def FirstLane (self):
        return self.__lane
            

beatrix = HEROES ("> Beatrix", "Marksman", "GoldLaner")

print("\n>>> Data Awal <<<")
print("- Role Awal : ", beatrix._HEROES__lane)
print(beatrix.AllInfo())

#cara untuk mengambil data lane walaupun dijadiin private
print("\n<<< Update Lane >>>")
beatrix.__lane = "MidLaner" #gabisa
beatrix._HEROES__lane = "MidLaner"
print("- Update Lane : ", beatrix._HEROES__lane)
print(beatrix.AllInfo())

#method 4
#cara sederhana mengambil data lane
print("\n--- Cara Lain ---")
print(beatrix.FirstLane())


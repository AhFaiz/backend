class trying :
    def __init__ (self):
        print("=== Latihan Method ===")
        
latihan = trying()

class BIODATA :
    
    def __init__ (self, name, role, lane):
        self.name       = name
        self.role       = role
        self.lane       = lane
    
    #method mengubah nama    
    def update_name (self, new_name):
        if self.name != "Hylos" :
            self.name = new_name
    
    #method mengubah gender
    def update_role (self, new_role):
        self.role = new_role
        
    #method mengubah place
    def update_lane (self, new_lane):
        self.lane = new_lane
        
    def AllInfo (self):
        return f"{self.name} - {self.role} - {self.lane}"
        
hylos  = BIODATA ("Hylos", "Tank", "MidLaner")
beatrix = BIODATA ("Beatrix", "Marksman", "Goldlaner")

#============== HYLOS =================
print("\n--- Biodata Hylos ---")
print("Name : ",hylos.name)
print("Role : ",hylos.role)
print("Lane : ",hylos.lane)
print("All Data : ",hylos.AllInfo())

print("\n>>> Hylos's Data After Updated <<<")
#update hylos"s name
hylos.update_name("YuZhong")
print("- New Name :", hylos.name)

#update hylo's role
hylos.update_role ("Fighter")
print("- New Role :", hylos.role)

#update hylo's lane
hylos.update_lane ("Explaner")
print("- New Lane : ", hylos.lane)

#All Data of Hylos After Updated
print("- Data Updated : ", hylos.AllInfo())

#============== BEATRIX ==============
print("\n--- Biodata Beatrix ---")
print("- Name : ",beatrix.name)
print("- Role : ",beatrix.role)
print("- Lane : ",beatrix.lane)
print("- All Data : ",beatrix.AllInfo())

print("\n>>> Beatrix's Data After Updated <<<")

#update beatrix's name
beatrix.update_name ("Karrie")
print("- New Name : ", beatrix.name)

#update beatrix's role
beatrix.update_role ("Tank")
print("- New Role : ", beatrix.role)

#update beatrix's lane
beatrix.update_lane ("Goldlaner")
print("- New Lane : ", beatrix.lane)

print("- All Data : ", beatrix.AllInfo())


    
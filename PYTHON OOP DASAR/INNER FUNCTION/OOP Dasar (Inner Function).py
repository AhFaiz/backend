class JUDUL:
    def __init__ (self):
        print("--- Inner Function ---")
        
belajar = JUDUL()

print("========= BENTUK 1 =============")

class ITEM :
    def __init__ (self, item, price, place):
        self.item  = item
        self.price = price
        self.place = place 
        
    def info(self):
        def print_item():
            print(f"- Item  : {self.item}")
            
        def print_price():
            print(f"- Price : {self.price}")    
        
        def print_place():
            print(f"- Place : {self.place}")
    
        print_item()
        print_price()
        print_place()
        
item = ITEM ("Kursi", 500000, "IKEA Taman Anggrek")
item.info()

print("\n========= BENTUK 2 =============\n")

class HERO :
    def __init__ (self, name, role, lane):
        self.name = name
        self.role = role
        self.lane = lane
        
    def AllInfo(self):
        def print_name():
            return(f"- Name : {self.name}")
            
        def print_role():
            return(f"- Role : {self.role}")
        
        def print_lane():
            return(f"- Lane : {self.lane}")
        
        def iterative_functions(*fungsi):
            for arg in fungsi:
                print(arg)
        return iterative_functions(print_lane(),print_name(),print_role())
hero = HERO ("Beatrix", "Marksman", "GoldLane")

role = hero.AllInfo()

 



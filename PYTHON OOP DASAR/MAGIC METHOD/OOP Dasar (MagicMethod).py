class MAGICMETHOD :
    def __init__ (self, item, price):
        self.item   = item 
        self.price  = price
        
    def __str__ (self):
        return f"{self.item} = {self.price}"
    
    def __eq__(self, other):
        return self.item == other.price
    
    def __gt__(self, other) :
        return self.price > other.price
    
    def __add__(self, other) :
        return self.price + other.price
    
Kursi = MAGICMETHOD ("Kursi", 50)
Meja  = MAGICMETHOD ("Meja",60)

print(Kursi)
print(Kursi == Meja)
print(Kursi > Meja)
print(Kursi + Meja)
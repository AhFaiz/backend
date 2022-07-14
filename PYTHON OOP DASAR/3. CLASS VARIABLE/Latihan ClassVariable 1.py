class judul:
    def __init__ (self):
        print("--- Latihan Class Variable ---")

NamaJudul = judul()

class EXSYNC :
    total = 0
    
    def __init__ (self, AllEmployees, Job):
        self.AllEmployees  = AllEmployees
        self.Job           = Job
        EXSYNC.total      += 1
        
    def all(self):
        return f"{self.AllEmployees} \n{self.Job}"
        
role = EXSYNC ("> Pace, Randi, Adam, Faiz, Wisnu", "> Makes\Clear Some Programs")

print(EXSYNC.total,"(-- PROGRAMER --) : ")
print(role.all())

role2 = EXSYNC ("> Neuvill , Ferdy", "> Makes Some Designs")

print(EXSYNC.total,"(-- DESIGNER --) : ")
print(role2.all())

role3 = EXSYNC ("> Raihan, Fido", "> Creat Some Contents Good")

print(EXSYNC.total,"(-- DIGITAL CREATOR --) : ")
print(role3.all())

role4 = EXSYNC ("> James, Seto", "> Managing/Protecting Some Data")

print(EXSYNC.total,"(-- DATABASE --) : ")
print(role4.all())


        
        

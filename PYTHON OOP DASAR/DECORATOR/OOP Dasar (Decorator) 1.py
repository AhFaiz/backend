class DECORATOR :
    def  __init__ (self):
        print("---- Decorator ----\n")
        
belajar = DECORATOR()

print("===== CONTOH 1 =====")

def info (func):
    def wrapper():
        print("*"*5)
        func()
        print("^"*5)
        
    return wrapper

def say_hello():
    print("Haiii")
    
say_hello() #yang lama
say_hello = info(say_hello)
say_hello() #yang baru


print("\n===== CONTOH 2 =====")
def programer (func):
    def wrapper():
        print("PACE")
        func()
        print("RANDI")
    
    return wrapper

def role():
    print("FRONTEND")
role = programer(role)
role()
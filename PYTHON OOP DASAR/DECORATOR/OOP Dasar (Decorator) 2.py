class DECORATOR:
    def __init__ (self):
        print("---- DECORATOR 2 ----")
        
belajar = DECORATOR()

print("==== CONTOH 1 ====\n")
def info(func):
    def wrapper():
        print("^"*5)
        func()
        print(">"*5)
    
    return wrapper

@info
def say_hello():
    print("- HAIII -")
    
say_hello()

print("\n==== CONTOH 2 ====")
def role(func):
    def wrapper():
        print("NEUVILL")
        func()
        print("FERDY")
        
    return wrapper

@role
def design():
    print("- UI -")    

design()
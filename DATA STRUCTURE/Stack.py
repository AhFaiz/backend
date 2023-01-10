class LatihanStack():

    def __init__(self, Name):
        self.name = Name
        

    def Title1():
        print(" === Elements pushed  === \n")
    
    def Title2():
        print("\n === Elements popped === \n")

    def Title3():
        print("\n=== The Result ===")
        

# user1 = LatihanStack("Adam")
# user2 = LatihanStack("Pace")
# user3 = LatihanStack("Wisnu")



LatihanStack.Title1()

list = []

def append():
    list.append("Adam")
    list.append("Pace")
    list.append("Wisnu")
append()

def elements():
    print(list)
    
elements()

LatihanStack.Title2()

def pop():
    print(list.pop())
    print(list.pop())
    print(list.pop())

pop()

LatihanStack.Title3()

def result():
    print(list)
result()

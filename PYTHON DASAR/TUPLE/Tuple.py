#TUPLE
# items are ordered, unchangeable, and allow duplicate values.

#Ordered :
#When we say that tuples are ordered, 
# it means that the items have a defined order, and that order will not change.

#Unchangeable
#Tuples are unchangeable, 
#meaning that we cannot change, add or remove items after the tuple has been created.

#Create Tuple With One Item
#To create a tuple with only one item, 
#you have to add a comma after the item, 
#otherwise Python will not recognize it as a tuple.

#Tuple Items - Data Types
#Tuple items can be of any data type:



print ("=== CONTOH 1 ===")
data_tuples = (7,8,9,10,11)
print(data_tuples)
print(data_tuples[3])

#==============================

print ("\n=== CONTOH 2 ===")
names = ("RANDI", "PACE", "WISNU", "JUPRI", "JAMES")
print(names)

#==============================

print ("\n=== CONTOH 3 (TUPLE LENGTH) ===")
names = ("RANDI", "PACE", "WISNU", "JUPRI", "JAMES")
print(len(names))

#==============================


print ("\n=== CONTOH 4 (Tuple One Item)===")
name = ("RANDI",)
print(name)

#it's not tuple
print ("\n-- NOT TUPLE --")
name = ("WISNU")
print(name)

#==============================

print ("\n === CONTOH 5 (Any Data Types)=== ")
str         = ("RANDI", "PACE", "WISNU")
int         = (7,8,9,10,11)
bool        = (True, False)

tuple = str, int, bool

for type in tuple:
    print(type)
    
#==============================
    
print ("\n === CONTOH 6 (Contain Different Data)=== ")
tuple  = (0, "RANDI", 1, "PACE", 2,  "WISNU", True)
print(tuple)








#Change Tuple Values
#Once a tuple is created, you cannot change its values. 
# Tuples are unchangeable, or immutable as it also is called.

#But there is a workaround. 
# You can convert the tuple into a list, change the list, 
# and convert the list back into a tuple.

print("=== PROGRAM 1 (Change the Item)===")
x = ("RANDI", "PACE", "WISNU")
y = list(x)
y[1] = "JAMES"
x = tuple(y)

print(x)

#==========================================


print("\n=== PROGRAM 2 (Add the Item)===")

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

print(thistuple)

#==========================================

print("\n=== PROGRAM 3 (Add Tuple to  Tuple)===")

thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)


#1
nameUI = ["neuvill", "farid", "ojan"]
nameUI.remove("ojan")
#.remove to remove the banana"s item
print("\nHasil Program 1 = ", nameUI)


#2
nameUI = ["neuvill", "farid", "ojan"]
nameUI.pop(1)
#.pop to delete the index we want it
print("\nHasil Program 2 = ", nameUI)


#3
nameUI = ["neuvill", "farid", "ojan"]
nameUI.pop()
#remove the last item
print("\nHasil Program 3 = ", nameUI)


#4
nameUI = ["neuvill", "farid", "ojan"]
del nameUI[0]
#to remove the first item
print("\nHasil Program 4 = ", nameUI)


#5
nameUI = ["neuvill", "farid", "ojan"]
#remove the list
del nameUI


#6
nameUI = ["neuvill", "farid", "ojan"]
nameUI.clear()
#remove the item
print("\nHasil Program 5 = ", nameUI)

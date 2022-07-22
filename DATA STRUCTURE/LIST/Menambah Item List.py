#1
thislist = ["pace", "neuvill", "randi"]
thislist.append("wisnu")
#.append to add the item to the list and placed in the last
print("Hasil Program 1 = ", thislist)


#2
thislist = ["pace", "neuvill", "randi"]
thislist.insert(1, "wisnu")
#.insert to add the item to the list (the place is depends)
print("\nHasil Program 2 = ", thislist)


#3
frontend = ["pace", "randi", "wisnu"]
ui       = ["neuvill", "ferdy", "farid"]
frontend.extend(ui)
#.extendd to combine the first list and another list
print("\nHasil Program 3 = ", frontend)


#4
list1  = ["pace", "jupri", "neuvill"]
list2 = ("wisnu", "ferdy")
list1.extend(list2)
print("\nHasil Program 4 = ", list1)

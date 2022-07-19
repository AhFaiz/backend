#1
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)


#2
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
#the another way to Join List
list1.extend(list2)
print(list1)


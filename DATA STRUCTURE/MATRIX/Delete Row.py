from numpy import * 

print("=== PROGRAM 1 ====")

m = array([['Mon',18,20,22,17],['Tue',11,18,21,18],
   ['Wed',15,21,20,19],['Thu',11,20,22,21],
   ['Fri',18,17,23,22],['Sat',12,22,20,18],
   ['Sun',13,15,19,16]])

#Del index ke-2
m = delete(m,[2],0)

print(m)

print("\n=== PROGRAM 2 ====")

a = array([
    ['WISNU',10,11,12,13],
    ['RANDI',14,15,16,17],
    ['FAIZ',18,19,20,21],
    ['PACE',22,23,24,25],
    ['ADIT',26,27,28,29],
    ['REHAN',30,31,32,33],
    ['FIDHO',34,35,36,37]])

#Del Index Adit
a = delete(a,[4],0)

print(a)
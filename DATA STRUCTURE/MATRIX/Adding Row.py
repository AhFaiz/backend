from numpy import * 

print("=== PROGRAM 1 ====")

m = array([['Mon',18,20,22,17],['Tue',11,18,21,18],
   ['Wed',15,21,20,19],['Thu',11,20,22,21],
   ['Fri',18,17,23,22],['Sat',12,22,20,18],
   ['Sun',13,15,19,16]])

m_r = append(m,[['Avg',12,15,13,11]],0) #belakang ada 0, biar output kebawah sesuai index

print(m_r)

print("\n=== PROGRAM 2 ====")

a = array([
    ['WISNU',10,11,12,13],
    ['RANDI',14,15,16,17],
    ['FAIZ',18,19,20,21],
    ['PACE',22,23,24,25],
    ['ADIT',26,27,28,29],
    ['REHAN',30,31,32,33],
    ['FIDHO',34,35,36,37]])

x = append (a,[['FARID', 38, 39, 40, 41]],0)

print(x)


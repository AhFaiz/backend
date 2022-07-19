## --- LIST ---

# Kumpulan data numbers
data_angka = [1,5,2,3]
print("Data Angka        : ",data_angka)

# Kumpulan data string
data_string = ["NEUVILL","JUPRI","RANDI"]
print("\nData String       : ",data_string)

# Kumpulan data boolean
data_boolean = [True, False, False, True]
print("\nData Boolean      : ",data_boolean)

# Kumpulan campuran
data_campuran = [1,"NEUVILL",2,"PACE","RANDI",True,"ADAM",False]
print("\nData Campuran     : ",data_campuran)

## cara alternatif membuat list
data_range = range(0,12,2) # range(start,stop,step)
print("\nData Range        : ",data_range)

data_list = list(data_range)
print("\nData List         : ",data_list)

# membuat list dengan for loop, list comprehension
list_pake_for = [i**2 for i in range(0,10)]
print("\nList with For     : ",list_pake_for)

# membuat list pake for pake if
list_pake_for_if = [i for i in range(0,10) if i != 5]
print("\nList with For If  : ",list_pake_for_if)

list_pake_for_if = [i for i in range(0,10) if i%2 ==0]
print("\nBilangan Genap    : ",list_pake_for_if)

list_pake_for_if = [i**2 for i in range(0,10) if i%2 !=0]
print("\nBilangan Ganjil   : ",list_pake_for_if)
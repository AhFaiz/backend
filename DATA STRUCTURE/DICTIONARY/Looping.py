data_dict = {
	'BE':'FAIZ',
	'UI':'NEUVILL',
	'FE':'PACE',
	'FIN':'ADIT',
	'nmbr':18,
}

print("========= Program 1 =========\n")

#TAKE THE KEYS:
for x in data_dict:
    print("All Keys : ",x)

print("==================")

#TAKE THE KEYS(2)
for x in data_dict.keys():
  print("All Keys(2) : ",x)

print("\n========= Program 2 =========\n")

#TAKE THE VALUES
for x in data_dict:
    print("All Values : ",data_dict[x])
    
print("==================")

#TAKE THE VALUES(2)
for x in data_dict.values():
  print("All Values(2)",x)

print("\n========= Program 3 =========\n")

#TAKE THE KEY AND VALUES
for x in data_dict:
    print(f"Key =",x, ", Value =",data_dict[x])

print("==================")

#TAKE THE KEY AND VALUES(2)
for x, y in data_dict.items():
  print("Key :",x,", Value :",y)

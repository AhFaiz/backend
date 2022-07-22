data_dict = {
	'key':'value',
	'UI':'NEUVILL',
	'FE':'PACE',
	'FIN':'ADIT',
	'nmbr':18,
}

x = data_dict["UI"]
print("Cara 1: ",x)

#with the .get method
x = data_dict.get("FE")
print("\nWith Get Method :", x)

#access the keys
x = data_dict.keys()
print("\nKEYS : ",x)

#access the values
x = data_dict.values()
print("\nVALUES : ",x)



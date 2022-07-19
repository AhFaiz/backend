data_dict = {
	'key':'value',
	'UI':'NEUVILL',
	'FE':'PACE',
	'FIN':'ADIT',
	'nmbr':18,
}

x = data_dict["UI"]

print(x)

#with the .get method
x = data_dict.get("FE")
print(x)

#access the key
x = data_dict.keys()
print(x)

x = data_dict.values()
print(x)



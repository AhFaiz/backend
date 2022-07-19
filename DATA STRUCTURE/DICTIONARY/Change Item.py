data_dict = {
	'key':'value',
	'UI':'NEUVILL',
	'FE':'PACE',
	'FIN':'ADIT',
	'nmbr':18,
}

data_dict ["UI"]  = "FERDY"
print("Change Value from UI = ",data_dict)


#with update() method
data_dict.update({"FE" : "RANDI"})
print("\nChange The Value with Update : ", data_dict)
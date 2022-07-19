data_dict = {
	'key':'value',
	'UI':'NEUVILL',
	'FE':'PACE',
	'FIN':'ADIT',
	'nmbr':18,
}

data_dict.pop("FIN")
print("Remove with .pop Method: ",data_dict)

#with del keyword
del data_dict["FE"]
print("\nRemove With Del Keyword: ",data_dict)

data_dict.clear()
print("\nDelete All Dicts: ",data_dict)




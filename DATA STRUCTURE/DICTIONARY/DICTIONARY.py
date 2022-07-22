# list -> array, mengakses dengan  menggunakan index
data_list = ['NEUVILL','JUPRI','PACE']
print(data_list[0])

# dictionary (dict) -> associative array(mengakses data key)
data_dict = {
	'key':'value',
	'UI':'NEUVILL',
	'FE':'PACE',
	'FIN':'ADIT',
	'nmbr':18,
	'list':data_list,
}

print(data_dict)
print(data_dict['FE'])
print(data_dict['nmbr'])
print(data_dict['list'])

#dictionary not allowed to have two items with same key
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print("\n",thisdict)
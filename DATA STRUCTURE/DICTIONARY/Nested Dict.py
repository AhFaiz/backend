programmer1 ={
    "name"   : "Faiz",
    "role"   : "BackEnd",
    "age"    : 20,
    "year"   : 2001
},
programmer2 = {
    "name"   : "Randi",
    "role"   : "FrontEnd",
    "age"    : 20,
    "year"   : 2002
},
programmer3 = {
    "name"   : "Neuvil",
    "role"   : "UI",
    "age"    : 20,
    "year"   : 2002
}

EXSYNC = {
    "programmer1" : programmer1,
    "programmer2" : programmer2,
    "programmer3" : programmer3
    
}
for i in programmer1:
    j = i["name"]
    print(j)
    
print("===================================")    
    
jupri= {"programmer1" :{
    "name"   : "Faiz",
    "role"   : "BackEnd",
    "age"    : 20,
    "year"   : 2001
},
"programmer2" : {
    "name"   : "Randi",
    "role"   : "FrontEnd",
    "age"    : 20,
    "year"   : 2002
},
"programmer3" : {
    "name"   : "Neuvil",
    "role"   : "UI",
    "age"    : 20,
    "year"   : 2002
}}

for x,y in jupri.items():
    if x == "programmer1": 
        print(y["name"])
#CASTING 
#(merubah dari satu tipe ke tipe lain)

#1 DATA INTEGER
print("\n1.====INTEGER====")

data_int = 9
print("data = ", data_int, ",type =",type(data_int))

print("CASTING!!")
data_float = float(data_int)
print("data = ", data_float, ",type =",type(data_float))
data_str   = str(data_int)
print("data = ", data_str, ",type =",type(data_str))
data_bool  = bool(data_int)
print("data = ", data_bool, ",type =",type(data_bool))


#2 DATA FLOAT
print("\n2.====FLOAT====")

data_float = 10
print("data =", data_float, ",type =",type(data_float))

print("\nCASTING!!")
data_int = int(data_float)
print("data = ", data_int, ",type =",type(data_int))
data_str = str(data_float)
print("data = ", data_str, ",type =",type(data_str))
data_bool = bool(data_float)
print("data = ", data_bool, ",type =",type(data_bool))


#3 DATA BOOLEAN
print("\n3.====BOOLEAN====")
data_bool = False;
print("data = ", data_bool, ",type =",type(data_bool))

print("\nCASTING!!")
data_int = int(data_bool)
print("data = ",data_int, ",type =",type(data_int))
data_str = str(data_bool)
print("data = ",data_str,",type =",type(data_str))
data_float = float(data_bool)
print("data= ",data_float,",type =",type(data_float))


#4 DATA STRING
print("\n4.====STRING====")
data_str = "10"
print("data = ", data_str, ",type =",type(data_str))

print("\n====CASTING!!====")
data_int = int(data_str)
print("data = ",data_int, ",type =",type(data_int))
data_bool = bool(data_str)
print("data = ",data_bool, ",type =",type(data_bool))
data_float = float(data_str)
print("data = ",data_float, ",type =",type(data_float))
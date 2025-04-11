# mengubah satu tipe data ke bentuk yang lain
# 1 integer #float >>> integer, boolean >>> integer
data = 19.9
data_int = int(data)
print(data, type(data))
print(data_int, type(data_int))

# 2 float 
data = 10
data_float = int(data)
print(data, type(data))
print(data_float, type(data_float))

# to boolean
# dari float / int bisa berubah ke bolean
data = 10
data_convert = bool(data)
print(data, type(data))
print(data_convert, type(data_convert))
# string,list,set,tuple,dict bisa berubah ke data boolean
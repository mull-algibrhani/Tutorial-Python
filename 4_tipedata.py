from ctypes import c_double
print("---Type Data---")
# type data adalah jenis jenis data yang bisa kita masukkan kedalam variable

""" TYPE DATA UMUM PADA PYTHON """

# 1 type data angka (integer)
data_integer = 12
print("data :", data_integer, "bertype", type(data_integer))

# 2 type data karakter (string)
my_string = "nama saya mull"
my_double = 12.5
print("data :", my_string, "bertype", type(my_string))

# 3 type data bilangan pecahan/desimal (float)
data_float = 12.4
print("data :", data_float, "bertype", type(data_float))

# 4 type data list (list)
data_list = [1, 3, 2, 4]
buah = ["apple", "banana", "cherry"]
print("data :", data_list, "bertype", type(data_list))
print("data :", buah, "bertype", type(buah))

# 5 type data biner True/False  (boolean)
biner = True
print("data :", biner, "bertype", type(biner))

""" TYPE DATA KHUSUS PADA PYTHON """

# 5 type data kompleks (imaginer)
kompleks1 = complex(1, 5)
kompleks2 = complex(-12, 13)
print("data :", kompleks1, "bertype", type(kompleks1))
print("hasil kompleks1 + kompleks2 =", kompleks1 + kompleks2)

# 6 type data tuple
data_tuple = (1, 3, 2, 4)
data_tuple2 = ("apple", "banana", "cherry")
print("data :", data_tuple, "bertype", type(data_tuple))
print("data :", data_tuple2, "bertype", type(data_tuple2))

# 7 type data range
data_range = range(5)
print("data :", data_range, "bertype", type(data_range))

# 8 type data dictionary
data_dictionary = {"name": "mull", "umur": 24,
                   "alamat": "bantaeng", "jenis kelamin": "L"}, {"name": "amir", "umur": 45,
                                                                 "alamat": "malaysia", "jenis kelamin": "L"}
print("data :", data_dictionary, "bertype", type(data_dictionary))

# 9 type data set
data_set = {"apple", "banana", "cherry"}, {
    "ikan", "kepiting", "udang"}, {"kangkung", "bayam", "terong"}
print("data :", data_set, "bertype", type(data_set))


""" TYPE DATA DARI BAHASA C """
#  type data c_double
# import modul c dari phyton
data_cdouble = c_double(12.12345)
print("data :", data_cdouble, "bertype", type(data_cdouble))

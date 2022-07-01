# casting tipe data adalah merupa tipe data pada suatu variable
print("---casting tipe data---")

# casting variable tipe data integer
print("---CASTING TIPE DATA INTEGER---")
data_int = 21
data_float = float(data_int)
data_str = str(data_int)
data_bool = bool(data_int)
print("data :", data_float, "bertipe :", type(data_float))
print("data :", data_str, "bertipe :", type(data_str))
print("data :", data_bool, "bertipe :", type(
    data_bool))  # akan false juka nilai int = 0

# casting variable tipe data float
print("---CASTING TIPE DATA FLOAT---")
data_float = 9.7
data_int = int(data_float)  # angka akan dibulatkan kebawah
data_str = str(data_float)
data_bool = bool(data_float)
print("data :", data_float, "bertipe :", type(data_float))
print("data :", data_str, "bertipe :", type(data_str))
print("data :", data_bool, "bertipe :", type(
    data_bool))  # akan false juka nilai float = 0

# casting variable tipe data string
print("---CASTING TIPE DATA STRING---")
data_str = "12"
data_int = int(data_str)  # string harus berisi angka
data_float = float(data_str)  # string harus berisi angka
data_bool = bool(data_str)  # string harus berisi kosong untuk menjadi false
print("data :", data_int, "bertipe :", type(data_int))
print("data :", data_float, "bertipe :", type(data_float))
print("data :", data_bool, "bertipe :", type(
    data_bool))  #

# casting variable tipe data boolean
print("---CASTING TIPE DATA BOOLEAN---")
data_bool = True
data_int = int(data_bool)
data_float = float(data_bool)
data_str = str(data_bool)
print("data :", data_bool, "bertipe :", type(data_bool))
print("data :", data_float, "bertipe :", type(data_float))
print("data :", data_str, "bertipe :", type(
    data_str))

print(5*"=", "STRING WIDTH AND ALIGNMENT", 5*"=")

print("\n", 5*"=", "STRING MULTI STANDAR", 5*"=")
# string standar
nama = "Mull"
umur = 28
tinggi = 58.5
berat = 48
data = f"Nama : {nama}, Umur : {umur} tahun, Tinggi : {tinggi} cm, Berat Badan : {berat} kg"
print(data)

print("\n", 5*"=", "STRING MULTI LINE", 5*"=")
# string multi line menggunakan enter \n
data = f"Nama : {nama}, \nUmur : {umur} tahun, \nTinggi : {tinggi} cm, \nBerat Badan : {berat} kg"
print(data)

print("\n", 5*"=", "STRING MULTI LINE", 5*"=")
# string multi line menggunakan kutip triplets (""" """)
data = f"""Nama : {nama}
Umur : {umur} tahun
Tinggi : {tinggi} cm
Berat Badan : {berat} kg"""
print(data)

print("\n", 5*"=", "STRING MULTI LINE 2", 5*"=")
# string multi line menggunakan kutip triplets (""" """)
data = f"""Nama : {nama}, Umur : {umur} tahun
Tinggi : {tinggi} cm, Berat Badan : {berat} kg"""
print(data)

print("\n", 5*"=", "STRING MULTI LINE 3", 5*"=")
# string multi line menggunakan kutip triplets (""" """)
data = f"""
Nama : {nama}, Umur : {umur} tahun

Tinggi : {tinggi} cm, Berat Badan : {berat} kg
# -> menggunkan enter
"""
print(data)

print("\n", 5*"=", "MENGATUR BARIS DATA", 5*"=")
data = f"""
Nama        : {nama}
Umur        : {umur} tahun
Tinggi      : {tinggi} cm
Berat Badan : {berat} kg
"""
print(data)

print("\n", 5*"=", "MENGATUR LEBAR DATA", 5*"=")
data = f"""
Nama        : {nama:>8}
Umur        : {umur} tahun
Tinggi      : {tinggi:>5} cm
Berat Badan : {berat:>5} kg
"""
print(data)

# print("===OPERASI ARITMATIKA===")

# a = int(input("masukkan angka: "))
# b = int(input("masukkan angka: "))

# hasil_tambah = a + b
# hasil_kurang = a - b
# hasil_kali = a * b
# hasil_bagi = a / b
# hasil_exponen = a ** b
# hasil_modulus = a % b
# hasil_floor_division = a // b

# print("hasil : ", a, "+", b, "=", hasil_tambah)
# print("hasil : ", a, "-", b, "=", hasil_kurang)
# print("hasil : ", a, "x", b, "=", hasil_kali)
# print("hasil : ", a, "/", b, "=", hasil_bagi)
# print("hasil : ", a, "xx", b, "=", hasil_exponen)
# print("hasil : ", a, "%", b, "=", hasil_modulus)
# print("hasil : ", a, "//", b, "=", hasil_floor_division)

print("===OPERASI PRIORITAS===")
x = 3
y = 2
z = 4

# tanpa prioritas operasi
hasil = x ** y * z + x / y - y % z // x
print(hasil)

# dengan prioritas operasi dengan (akan dieksekusi pertama)
hasil = x ** y * (z + x) / y - y % z // x
print(hasil)

# tanpa prioritas operasi
hasil = x + y * z
print(hasil)

# dengan prioritas operasi dengan (akan dieksekusi pertama)
hasil = (x + y) * z
print(hasil)

"""
urutan operasi aritmatika
1. prioritas = ()
2. exponen = **
3. perkalian, pembagian, modulus dan floor division = *, /, %, //
4. penjumlahan dan pengurangan = +, -
"""

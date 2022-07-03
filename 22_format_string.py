print(5*"=" + " FORMAT STRING " + 5*"=")
# # melakukan format pada string
# nama = input('Masukkan Nama : ')
# umur = input('Masukkan Umur : ')
# print('nama : ' + nama, 'umur : ', int(umur))
# print(f"hello {nama}")
# print(f"umur kamu {umur} tahun")
# print(f"hello {nama}", f"umur kamu {umur} tahun")

# boolean
boolean = False
format_bool = f"boolean = {boolean}"
print(format_bool)

# angka
angka = 234.67
format_angka = f"angka = {angka}"
print(format_angka)

# bilangan dengan ordo ribuan
angka = 2000
format_angka = f"bilangan ribuan = {angka:,}"
print(format_angka)

# bilangan dengan ordo jutaan
angka = 200000
format_angka = f"bilangan ribuan = {angka:}"
print(format_angka)

# bilangan desimal dengan menetukan berapa angka dibelakang koma
angka = 200.4445
format_angka = f"bilangan ribuan = {angka:.2f}"
print(format_angka)

# bilangan desimal dengan pembulatan kebawah
angka = 200.4445
format_angka = f"bilangan ribuan = {angka:.0f}"
print(format_angka)
# bilangan desimal dengan pembulatan keatas
angka = 200.7445
format_angka = f"bilangan ribuan = {angka:.0f}"
print(format_angka)

# menampilkan leading zero
angka = 200.7445
format_angka = f"bilangan ribuan = {angka:09.3f}"
print(format_angka)

# menampilkan tanda - dan +
angka_minus = -10
angka_plus = +10
format_minus = f"angka minus = {angka_minus:+d}"
format_plus = f"angka plus = {angka_plus:+d}"
print(format_minus)
print(format_plus)

# format pesen
persen = 0.024
format_persen = f"persentase = {persen:.2%}"
print(format_persen)

# melakukan operasi aritmatika di dalam kurung
nama_brng = "beras"
harga = 15000
jumlah = 2
print("nama barang :", nama_brng)
print("jumlah barang :", jumlah)
print(f"harga barang : {harga:,}")
format_str = f"total harga = Rp. {harga*jumlah:,}"
print(format_str)

# format angka lain (binary, octal, hexadecimal)
angka = 255
format_binary = f"binery : {bin(angka)}"
format_octal = f"octal : {oct(angka)}"
format_hexa = f"hexa : {hex(angka)}"
print("format binery dari angka :", angka, "=", format_binary)
print("format octal dari angka :", angka, "=", format_octal)
print("format hexa dari angka :", angka, "=", format_hexa)

# # melakukan operasi aritmatika di dalam kurung dan casting variable untuk format integer
# nama_barang = input("masukkan nama barang: ")
# harga_barang = input("masukkan harga barang: ")
# jumlah_barang = input("masukkan jumlah barang: ")
# harga_barang = int(harga_barang)
# jumlah_barang = int(jumlah_barang)
# total = f"{harga_barang * jumlah_barang}"
# format_total_to_int = int(total)
# format_total_to_str = f"Total belanja : Rp. {format_total_to_int:,}"
# print("nama barang :", nama_barang)
# print("jumlah barang: ", jumlah_barang)
# print(f"harga barang: Rp. {harga_barang:,}")
# print(format_total_to_str)

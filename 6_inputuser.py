print("=== MENGAMBIL INPUT DARI USER ===")

nama = input("masukkan nama : ")
umur = int(input("masukkan umur : "))
jnis_klm = input("masukkan jenis kelamin : ")
nilai = float(input("masukkan nilai: "))
print("===DATA===")
print("Nama          :", nama, type(nama))
print("Umur          :", umur, type(umur))
print("Jenis Kelamin :", jnis_klm, type(jnis_klm))
print("Nilai :", nilai, type(nilai))

print("=== MENGAMBIL INPUT DARI USER DENGAN TIPE DATA BOLLEAN ===")

biner = bool(int(input("masukkan nilai boolean 1 atau 0: ")))
print("Nilai Biner: ", biner)

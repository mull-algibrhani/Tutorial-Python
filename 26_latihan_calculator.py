print(5*"="+" KALKULATOR "+5*"="+"\n")


angka_1 = float(input("Masukkan Angka Pertama : "))
operator = input("Masukkan Operator x / + - % : ")
angka_2 = float(input("Masukkan Angka Kedua : "))


if operator == "*" or aperator == "x":
    # hasil = angka_1 * angka_2
    print(f"Hasil : {angka_1*angka_2}")
elif operator == "+":
    # hasil = angka_1 + angka_2
    print(f"Hasil : {angka_1+angka_2}")
elif operator == "/":
    # hasil = angka_1 / angka_2
    print(f"Hasil : {angka_1/angka_2}")
elif operator == "-":
    # hasil = angka_1 - angka_2
    print(f"Hasil : {angka_1-angka_2}")
elif operator == "%":
    # hasil = angka_1 % angka_2
    print(f"Hasil : {angka_1%angka_2}")
else:
    print("Operator Tidak Ditemukan")

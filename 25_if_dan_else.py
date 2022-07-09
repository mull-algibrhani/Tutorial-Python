print(5*"="+" IF, ELSE DAN ELIF "+5*"="+"\n")

print("Cek Nama")
input_name = input("Masukkan Nama : ")
if input_name == 'mull':
    print("Nama Kamu Terdaftar")
elif input_name == 'leni':
    print("Nama Kamu Terdaftar")
    umur_leni = int(input(f"masukkan umur {input_name}: "))
    if umur_leni <= 17:
        print(f"umur {input_name} belum cukup")
    else:
        print(f"umur {input_name} sudah cukup")
elif input_name == 'ucup':
    print("Nama Kamu Terdaftar")
    umur_ucup = int(input(f"masukkan umur {input_name}: "))
    if umur_ucup <= 17:
        print(f"umur {input_name} belum cukup")
    else:
        print(f"umur {input_name} sudah cukup")
else:
    print("Nama Kamu tidak terdaftar")

# if dengan inline
print("\n5 + 2 sama dengan berapa.?")
jawab = int(input("Jawaban :"))
if jawab == 7:
    print("jawaban yang kamu masukkan benar")

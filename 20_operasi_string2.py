print('=======OPERASI DAN MANIPULASI STRING PART 2=====')

print('\n======OPERASI DALAM BENTUK METHOD====')
# Merubah string to upper case

salam = 'Assalamu Alaikum Warahmatullahi Wabarakatu'
print('Normal : ', salam)
print('UPPER : ', salam.upper())
print('lower : ', salam.lower())

# pengecekan case lower pada string
salam = 'assalamu alaikum'
cek = salam.islower()
print(salam, 'adalah lower = ', cek)

# pengecekan case upper pada string
salam = 'assalamu alaikum'
cek = salam.isupper()
print(salam, 'adalah upper = ', cek)

# menghapus space di awal string
salam = " assalamu, alaikum"
print(salam.strip())

# replace karakter pada string
salam = "assalamu, alaikum"
print(salam.replace('a', 'A'))

# melakukan split/memisahkan string
salam = "assalamu, alaikum, warahmatullahi"
split_salam = salam.split(',')
print(salam, type(split_salam))

# melakukan join/mengabungkan string
salam2 = ["assalamu", "alaikum", "warahmatullahi"]
# join dengan tanda koma ,
join_salam = ','.join(salam2)
print(join_salam, type(join_salam))
# join dengan space ' '
join_salam = ' '.join(salam2)
print(join_salam, type(join_salam))

# format pada string dari int
umur = 25
kelas = 2
no_hp = 199
teks = 'nama saya musliadi umur saya {} tahun, saya sudah kelas {} SD, nomor handphone saya {}'
print(teks.format(umur, kelas, no_hp))  # harus sesuai urutan variable
# hasil dengan tidak sesuai urutan variable
print(teks.format(umur, no_hp, kelas))

# string dengan octal value
txt = "\110\145\154\154\157"
print(r"karakter dari oktal \110\145\154\154\157 adalah :", txt)

# string dengan hex value
txt = "\x48\x65\x6c\x6c\x6f"
print(r"karakter dari Hex \x48\x65\x6c\x6c\x6f adalah :", txt)

# mengecek komponen string dengan startswith() dan endswith()
text = "Hello, welcome to my world."
hasil = text.startswith("hello")
print('apakah ada kata hello diawal :', hasil)
text = "Hello, welcome to my world."
hasil = text.endswith("world.")
print('apakah ada kata world. di akhir : ', hasil)

# alokasi karakter dengan rjust(), ljust(), center()
# justify kanan
kata = "selamat sore"
rata_kanan = kata.rjust(18, '=')
print("'", rata_kanan, "'")
# menghilangkan justyfi dengan strip()
print(rata_kanan.strip('='))

# justify kiri
kata = "selamat sore"
rata_kiri = kata.ljust(18)
print("'", rata_kiri, "'")
# menghilangkan justyfi dengan strip()
print(rata_kiri.strip())

# justify center
kata = "selamat sore"
rata_tengah = kata.center(18, '=')
print("'", rata_tengah, "'")
# menghilangkan justyfi dengan strip()
print(rata_tengah.strip('='))

# capitalize
print(kata.capitalize())
# title
print(kata.title())

# =====FUNGSI ATAU METHOD LAINNYA===== #
# isalpha() --> untuk mengecek apakah semuanya adalah huruf ?
# isalnum() --> untuk mengecek apakah semuanya adalah huruf dan angka?
# isdecimal() --> untuk mengecek apakah semuanya angka?
# isspace() --> untuk mengecek apakah ada space, tab, atau enter?
# istitle() --> untuk mengecek apakah dimulai dari huruf kapital?
# method string lainnya dapat dicek di : https://www.w3schools.com/python/python_strings_methods.asp

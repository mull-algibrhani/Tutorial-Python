print('===LATIHAN KOMPARASI LOGIKA===')
# soal
# ++++++0------5++++++8-----11++++++
userInput = float(input(
    'masukkan angka lebih kecil dari 0 dan lebih besar dari 5 atau lebih kecil dari 8 dan lebih besar dari 11 :'))

# ++++++0---------
# memeriksa angka lebih kecil dari 0
islebihdari0 = (userInput < 0)
print('lebih kecil  dari 0 = ', islebihdari0)

# ---------5++++++++++
# memeriksa angka lebih besar dari 5
islebihdari5 = (userInput > 5)
print('lebih besar  dari 5 = ', islebihdari5)

# ++++++8---------
# memeriksa angka lebih kecil dari 8
islebihdari8 = (userInput < 8)
print('lebih kecil  dari 8 = ', islebihdari8)

# -------11+++++++++
# memeriksa angka lebih besar dari 11
islebihdari11 = (userInput > 11)
print('lebih besar  dari 11 = ', islebihdari11)

hasil = islebihdari0 or islebihdari5 and islebihdari8 or islebihdari11

# membuat fungsi pengecekan dengan if
print('angka yang anda masukkan adalah : ', hasil)
if hasil == True:
    print("Jawaban yang anda masukkan benar !")
else:
    print("Maaf Jawaban anda salah !")

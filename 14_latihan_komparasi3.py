print('===LATIHAN KOMPARASI LOGIKA===')
# soal
# ------0++++++5-----8++++++++11------
userInput = float(input(
    'masukkan angka lebih besar dari 0 dan lebih kecil dari 5 atau lebih besar dari 8 dan lebih kecil dari 11 :'))

# -------0+++++++
# memeriksa angka lebih besar dari 0
islebihdari0 = (userInput > 0)
print('lebih besar  dari 0 = ', islebihdari0)

# -------5+++++++
# memeriksa angka lebih kecil dari 5
islebihdari5 = (userInput < 5)
print('lebih besar  dari 5 = ', islebihdari5)

# -------8+++++++
# memeriksa angka lebih besar dari 8
islebihdari8 = (userInput > 8)
print('lebih besar  dari 8 = ', islebihdari8)

# -------11+++++++
# memeriksa angka lebih kecil dari 11
islebihdari11 = (userInput < 11)
print('lebih besar  dari 11 = ', islebihdari11)

# # ------0++++++5-----8++++++++11------
# memeriksa hasil lebih besar dari 0 dan lebih kecil dari 5 atau lebih besar dari 8 dan lebih kecil dari 11
hasil = islebihdari0 and islebihdari5 or islebihdari8 and islebihdari11
print('angka yang anda masukkan adalah : ', hasil)

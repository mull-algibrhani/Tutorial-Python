print('===LATIHAN KOMPARASI LOGIKA===')

inputuser = float(
    input('masukkan angka lebih besar dari 5 atau lebih kecil dari 10 : '))
# ------5+++++++10-------

# -------5+++++++
# memeriksa angka lebih besar dari 5
islebihdari = (inputuser > 5)
print('lebih besar  dari 5 = ', islebihdari)

# -------------------10+++++++
# memeriksa angka lebih kecil dari 10
iskurangdari = (inputuser < 10)
print('lebih kecil dari 10 = ', iskurangdari)

# ++++++++5---------10+++++++
# memeriksa hasil lebih besar dari 5 dan lebih kecil dari 10
hasil = islebihdari and iskurangdari
print('angka yang anda masukkan adalah : ', hasil)

print('===LATIHAN KOMPARASI LOGIKA===')

inputuser = float(
    input('masukkan angka lebih kecil dari 5 atau lebih besar dari 10 : '))
# ++++++++5---------10+++++++

# ++++++++5------------------
# memeriksa angka kurang dari 5
iskurangdari = (inputuser < 5)
print('kurang dari 5 = ', iskurangdari)

# -------------------10+++++++
# memeriksa angka lebih dari 10
islebihdari = (inputuser > 10)
print('lebih dari 10 = ', islebihdari)

# ++++++++5---------10+++++++
# memeriksa hasil lebih kecil dari 5 dan lebih besar dari 10
hasil = iskurangdari or islebihdari
print('angka yang anda masukkan adalah : ', hasil)

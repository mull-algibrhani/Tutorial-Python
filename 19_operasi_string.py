print('=======OPERASI DAN MANIPULASI STRING=====')

print('=======MENYAMBUNG STRING (CONCATENATE)=====')
first_name = "Mull"
midle_name = "Al"
last_name = "Gibrhani"
print('Nama Saya : ', first_name + midle_name + last_name)
print('Nama Saya : ', first_name + ' ' + midle_name + ' ' + last_name)

print('\n=======MENGHITUNG PANJANG/JUMLAH STRING=====')
full_name = first_name + ' ' + midle_name + ' ' + last_name
print('Data : ', full_name)
print('Jumlah Karakter : ', len(full_name))

print('\n=======MENGECEK KARAKTER PADA STRING=====')
# mengecek apakah ada karakter tersebut dengan -> in
full_name = first_name + ' ' + midle_name + ' ' + last_name
cek_karakter = "d"
status = cek_karakter in full_name
print('Status : ', status)
# mengecek karakter pada string dengan funsi if
if status == True:
    print('karakter : ', cek_karakter, 'ada pada nama : ', full_name)
else:
    print('karakter : ', cek_karakter, 'tidak ada pada nama : ', full_name)
print('\n')
# mengecek apakah tidak ada karakter tersebut dengan -> not in
full_name = first_name + ' ' + midle_name + ' ' + last_name
cek_karakter = "d"
status = cek_karakter not in full_name
print('Status : ', status)
# mengecek karakter pada string dengan funsi if
if status == False:
    print('karakter : ', cek_karakter, 'ada pada nama : ', full_name)
else:
    print('karakter : ', cek_karakter, 'tidak ada pada nama : ', full_name)


print('\n=======MENGULANG STRING=====')
print('ha ' * 10)
print(12 * 'no ')

print('\n=======INDEXING STRING=====')
nama_saya = "mull al gibrhani"
print(nama_saya)
print('index ke 5 ', nama_saya, 'adalah : ' + nama_saya[5])
print('index ke (-1) ', nama_saya, 'adalah : ' + nama_saya[-1])
print('index ke (0 sampai 3) ', nama_saya, 'adalah : ' + nama_saya[0:3])
print('index ke (0 sampai 4) ', nama_saya, 'adalah : ' + nama_saya[0:4])
print('index ke (3 sampai 7) ', nama_saya, 'adalah : ' + nama_saya[3:8])
print('index ke (0,2,3,4,5,6,7,8,9,10) ',
      nama_saya, 'adalah : ' + nama_saya[0:10:2])

print('\n=======MIN DAN MAX STRING=====')
print('karakter paling kecil :', min(nama_saya))
print('karakter paling besar :', max(nama_saya))

print('\n=======LATIHAN KOMPARASI STRING=====')
nama_belakang1 = nama_saya[5:7]
nama_belakang2 = nama_saya[8:16]
hasil = nama_belakang1 + nama_belakang2
print(hasil)

('\n=======ASCI CODE STRING=====')
asci_code = ord('c')
print('asci code dari karakter c adalah :', str(asci_code))
data = 90
print('karakter dari 90 adalah :', chr(data))

print('\n=======OPERATRO STRING DALAM BENTUK METHOD=====')
kata = " darah muda darahnya para remaja"
jumlah_a = kata.count('a')
print('jumlah a dalam kata : ', kata, 'yaitu : ', jumlah_a)

print('\n')

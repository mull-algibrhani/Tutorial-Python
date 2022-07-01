print('===LATIHAN OPERASI ARITMATIKA===')
# LATIHAN KONVERSI SATUAN TEMPERATUR
print('\n===KONVERSI CELCIUS===\n')

celcius = float(input('masukkan suhu dalam celcius: '))
print('suhu dalam celcius adalah :', celcius, "celcius")


print('\n===KONVERSI KE REAMUR===\n')
# rumus 4/5 x celcius
reamur = (4/5) * celcius
print('suhu dalam reamur adalah :', reamur, "reamur")

print('\n===KONVERSI KE FAHRENHEIT===\n')
# rumus 9/5 x celcius + 32
fahrenheit = ((9/5) * celcius) + 32
print('suhu dalam fahrenheit adalah :', fahrenheit, "fahrenheit")

print('\n===KONVERSI KE KELVIN===\n')
# rumus celcius + 273
kelvin = celcius + 273
print('suhu dalam kelvin adalah :', kelvin, "kelvin")

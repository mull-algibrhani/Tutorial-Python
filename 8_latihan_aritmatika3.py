print('===KONVERSI SUHU KELVIN')
kelvin = (float(input('masukkan suhu dalam kelvin: ')))
print('suhu dalam kelvin adalah : ', kelvin, 'kelvin')

print('===\nKONVERSI SUHU KELVIN KE CELCIUS==\n')
# rumus = kelvin - 273.15
celcius = kelvin - 273.15
print('suhu dalam celcius adalah: ', celcius, 'celcius')

print('===\nKONVERSI SUHU KELVIN KE FAHRENHEIT==\n')
# rumus  = kelvin × 9/5 - 459.67
fahrenheit = (kelvin * 9/5) - 459.67
print('suhu dalam fahrenheit adalah: ', fahrenheit, 'fahrenheit')

print('===\nKONVERSI SUHU KELVIN KE REAMUR==\n')
# rumus  = 4/5 (kelvin - 273)
reamur = 4/5 * (kelvin - 273)
print('suhu dalam reamur adalah: ', reamur, 'reamur')

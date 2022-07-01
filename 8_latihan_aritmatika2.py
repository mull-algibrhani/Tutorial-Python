print('===KONVERSI SUHU FAHRENHEIT===')
fahrenheit = float(input('masukkan suhu fahrenheit: '))
print('suhu dalam fahrenheit adalah: ', fahrenheit, 'fahrenheit')

print('===\nKONVERSI SUHU FAHRENHEIT KE CELCIUS==\n')
# rumus = 5/9 * fahrenheit - 32
celcius = (5/9) * (fahrenheit - 32)
print('suhu dalam celcius adalah : ', celcius, 'celcius')

print('===\nKONVERSI SUHU FAHRENHEIT KE KELVIN==\n')
# Rumus = Fahrenheit + 459.67 × 5/9
kelvin = (fahrenheit + 459.67) * 5/9
print('suhu dalam kelvin adalah : ', kelvin, 'kelvin')

print('===\nKONVERSI SUHU FAHRENHEIT KE REAMUR==\n')
# Rumus = 4/9 * fahrenheit - 32
reamur = 4/9 * (fahrenheit - 32)
print('suhu dalam reamur adalah : ', reamur, 'reamur')

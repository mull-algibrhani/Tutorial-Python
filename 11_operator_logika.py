print('===OPERATOR LOGIKA===')
# and, or, not, xor
print('\n===OPERATOR NOT===')
a = True
b = not a
print('Data b = ', b)

a = False
b = not a
print('Data b = ', b)

print('\n===OPERATOR OR===')
# jika salah satu bernilai true maka hasilnya adalah true
# jika keduanya bernilai tru maka hasilnya adalah true
# jika keduanya bernilai false maka hasilnya adalah false
a = True
b = False
c = a or b
print(a, 'OR', b, '=', c)

a = False
b = True
c = a or b
print(a, 'OR', b, '=', c)

a = True
b = True
c = a or b
print(a, 'OR', b, '=', c)

a = False
b = False
c = a or b
print(a, 'OR', b, '=', c)

print('\n===OPERATOR AND===')
# jika salah satu bernilai false maka hasilnya adalah false
# jika keduanya bernilai tru maka hasilnya adalah true
# jika keduanya bernilai false maka hasilnya adalah false
a = True
b = False
c = a and b
print(a, 'AND', b, '=', c)

a = False
b = True
c = a and b
print(a, 'AND', b, '=', c)

a = True
b = True
c = a and b
print(a, 'AND', b, '=', c)

a = False
b = False
c = a and b
print(a, 'AND', b, '=', c)

print('\n===OPERATOR XOR===')
# jika salah satu bernilai true maka hasilnya adalah true
# jika keduanya bernilai tru maka hasilnya adalah false
# jika keduanya bernilai false maka hasilnya adalah false
a = True
b = False
c = a ^ b
print(a, 'XOR', b, '=', c)

a = False
b = True
c = a ^ b
print(a, 'XOR', b, '=', c)

a = True
b = True
c = a ^ b
print(a, 'XOR', b, '=', c)

a = False
b = False
c = a ^ b
print(a, 'XOR', b, '=', c)

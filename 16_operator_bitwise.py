print('===== OPERATOR BITWISE =====')

a = 9
b = 5

print('\n===== BITWISE OR (|) =====')
c = a | b
print('nilai :', a, 'binary :', format(a, '08b'))
print('nilai :', b, 'binary :', format(b, '08b'))
print('-------HASIL OR (|)-----------')
print('nilai :', c, 'binary :', format(c, '08b'))

print('\n===== BITWISE AND (&) =====')
c = a & b
print('nilai :', a, 'binary :', format(a, '08b'))
print('nilai :', b, 'binary :', format(b, '08b'))
print('-------HASIL AND (&)-----------')
print('nilai :', c, 'binary :', format(c, '08b'))

print('\n===== BITWISE XOR (^) =====')
c = a ^ b
print('nilai :', a, 'binary :', format(a, '08b'))
print('nilai :', b, 'binary :', format(b, '08b'))
print('-------HASIL XOR (^)-----------')
print('nilai :', c, 'binary :', format(c, '08b'))

print('\n===== BITWISE NOT (~) =====')
c = ~ a
print('nilai :', a, 'binary :', format(a, '08b'))
print('nilai :', b, 'binary :', format(b, '08b'))
print('-------HASIL NOT (~)-----------')
print('nilai :', c, 'binary :', format(c, '08b'))
print('-------HASIL NOT TO XOR (^)-----------')
d = 0b0000001001
e = 0b1111111111
print('nilai :', e ^ d, 'binary :', format(e ^ d, '08b'))

print('\n===== SIFTING RIGTH (>>) =====')
c = a >> 2
print('nilai :', a, 'binary :', format(a, '08b'))
print('-------HASIL SIFT RIGTH (>>)-----------')
print('nilai :', c, 'binary :', format(c, '08b'))

print('\n===== SIFTING LEFT (<<) =====')
c = a << 2
print('nilai :', a, 'binary :', format(a, '08b'))
print('-------HASIL SIFT LEFT (<<)-----------')
print('nilai :', c, 'binary :', format(c, '08b'))

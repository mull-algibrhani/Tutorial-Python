print('======OPERATOR ASSIGNMENT=======')
# operator assingment adalah operasi yang dapat dilakukan dengan penyingkatan
# atau operasi ditambah dengan assignment

a = 9  # ini adalah assignment
print('nilai a =', a)

# a = a ** 2  # ini adalah operasi
# print('nilai a =', a)

# x = 5
# x **= 3 # 5*5*5
# print(x)

# a = a + 2  # ini adalah operasi
# print('nilai a =', a)

# a = a - 2  # ini adalah operasi
# print('nilai a =', a)

# a = a * 2  # ini adalah operasi
# print('nilai a =', a)

# a = a / 2  # ini adalah operasi
# print('nilai a =', a)

# a = a % 2  # ini adalah operasi
# print('nilai a =', a)

# a = a // 2  # ini adalah operasi
# print('nilai a =', a)

a **= 2  # ini artinya sama dengan a = a ** 2
print('nilai a ** 2 adalah :', int(a))
a += 2  # ini artinya sama dengan a = a + 2
print('nilai a += 2 adalah :', a)

a -= 2  # ini artinya sama dengan a = a - 2
print('nilai a -= 2 adalah :', a)

a *= 2  # ini artinya sama dengan a = a * 2
print('nilai a *= 2 adalah :', a)

a /= 2  # ini artinya sama dengan a = a / 2
print('nilai a /= 2 adalah :', a)

a %= 2  # ini artinya sama dengan a = a % 2
print('nilai a % 2 adalah :', int(a))

a //= 2  # ini artinya sama dengan a = a // 2
print('nilai a // 2 adalah :', int(a))

a **= 2  # ini artinya sama dengan a = a ** 2
print('nilai a ** 2 adalah :', int(a))


print('====OPERASI ASSIGNMENT BITWISE OR(|=)=====')
b = True
print('nilai b =', b)
# OR (|)
print('\n=======True |= False=====')
b = True
b |= False
print('nilai b |= False, nilai b menjadi :', b)

print('\n=======False |= True=====')
b = False
b |= True
print('nilai b |= True, nilai b menjadi :', b)

print('\n=====False |= False=====')
b = False
b |= False
print('nilai b |= False, nilai b menjadi :', b)

print('\n=====True |= True=====')
b = True
b |= True
print('nilai b |= True, nilai b menjadi :', b)

print('\n====OPERASI ASSIGNMENT BITWISE AND(&=)=====')
b = True
print('nilai b =', b)
# AND (&)
print('\n=======True &= False=====')
b = True
b &= False
print('nilai b &= False, nilai b menjadi :', b)

print('\n=======False &= True=====')
b = False
b &= True
print('nilai b &= True, nilai b menjadi :', b)

print('\n=====False &= False=====')
b = False
b &= False
print('nilai b &= False, nilai b menjadi :', b)

print('\n=====True &= True=====')
b = True
b &= True
print('nilai b &= True, nilai b menjadi :', b)

print('\n====OPERASI ASSIGNMENT BITWISE XOR(^=)=====')
b = True
print('nilai b =', b)
# XOR (^)
print('\n=======True ^= False=====')
b = True
b ^= False
print('nilai b ^= False, nilai b menjadi :', b)

print('\n=======False ^= True=====')
b = False
b ^= True
print('nilai b ^= True, nilai b menjadi :', b)

print('\n=====False ^= False=====')
b = False
b ^= False
print('nilai b ^= False, nilai b menjadi :', b)

print('\n=====True ^= True=====')
b = True
b ^= True
print('nilai b ^= True, nilai b menjadi :', b)

print('\n====OPERASI ASSIGNMENT SIFTING=====')
d = 0b0100
print('nilai d =', format(d, '04b'))
# sifting rigth >>
d >>= 2
print('nilai d >>= 2', 'nilai d menjadi', format(d, '04b'))
# sifting left >>
d <<= 1
print('nilai d <<= 1', 'nilai d menjadi', format(d, '04b'))

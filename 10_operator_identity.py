print('=== OPERATOR IDENTITY ===')
a = 4
b = 2

c = 2
d = 4
# 'is' komparasi dengan 2 buah object identity
print('===KOMPARASI OBJECT IDENTITY DENGAN IS===')
print('nilai a = ', a, 'id = ', hex(id(a)))
print('nilai d = ', d, 'id = ', hex(id(d)))
hasil_is1 = a is d
hasil_is2 = a is b
print(a, 'is', d, '=', hasil_is1)
print(a, 'is', b, '=', hasil_is2)

# 'is NOT' komparasi dengan 2 buah object identity
print('===KOMPARASI OBJECT IDENTITY DENGAN IS NOT===')
print('nilai a = ', a, 'id = ', hex(id(a)))
print('nilai d = ', d, 'id = ', hex(id(d)))
hasil_is1 = a is not d
hasil_is2 = a is not b
print(a, 'is', d, '=', hasil_is1)
print(a, 'is', b, '=', hasil_is2)

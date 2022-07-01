print('=== OPERATOR KOMPARASI ===')
# operator komparasi adalah setiah hasil dari operator komparasi merupakan nilai boolean true or false

a = 4
b = 2

c = 2
d = 4
# lebih besar dari >
print('===LEBIH BESAR DARI===')
hasil1 = a > b
hasil2 = c > b
hasil3 = d > a
print(a, 'lebih besar dari', b, '=', hasil1)
print(c, 'lebih besar dari', d, '=', hasil2)
print(d, 'lebih besar dari', a, '=', hasil3)

# lebih kecil / kurang dari <
print('===KURANG DARI===')
hasil1 = a < b
hasil2 = c < d
hasil3 = d < a
print(a, 'kurang dari', b, '=', hasil1)
print(c, 'kurang dari', d, '=', hasil2)
print(d, 'kurang dari', a, '=', hasil3)

# lebih dari sama dengan >=
print('===LEBIH DARI SAMA DENGAN===')
hasil1 = a >= b
hasil2 = c >= d
hasil3 = d >= a
print(a, 'lebih dari sama dengan', b, '=', hasil1)
print(c, 'lebih dari sama dengan', d, '=', hasil2)
print(d, 'lebih dari sama dengan', a, '=', hasil3)

# kurang dari sama dengan <=
print('===KURANG DARI SAMA DENGAN===')
hasil1 = a <= b
hasil2 = c <= d
hasil3 = d <= a
print(a, 'kurang dari sama dengan', b, '=', hasil1)
print(c, 'kurang dari sama dengan', d, '=', hasil2)
print(d, 'kurang dari sama dengan', a, '=', hasil3)

# sama dengan ==
print('===SAMA DENGAN===')
hasil1 = a == b
hasil2 = c == d
hasil3 = d == a
print(a, 'sama dengan', b, '=', hasil1)
print(c, 'sama dengan', d, '=', hasil2)
print(d, 'sama dengan', a, '=', hasil3)

# tidak sama dengan !=
print('===TIDAK SAMA DENGAN===')
hasil1 = a != b
hasil2 = c != d
hasil3 = d != a
print(a, 'tidak sama dengan', b, '=', hasil1)
print(c, 'tidak sama dengan', d, '=', hasil2)
print(d, 'tidak sama dengan', a, '=', hasil3)

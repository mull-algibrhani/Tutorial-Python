print('===========STRING===========')
data = 'ini adalah string'
print(data)
print(type(data))

print('\n=====STRING DENGAN SINGLE QUOTE========')
data = 'ini adalah string dengan single quotw'
print(data)
print("'string single quote : ' '")

print('\n=====STRING DENGAN DOUBLE QUOTE========')
data = "ini adalah string dengan double quote"
print(data)
print('"string double quote : " "')

print('\n=====STRING DENGAN SLASH========')
data = 'hari ini adalah hari jum\'at '
print(data)
print(" string dengan slash : " '\'\'')

print('\n=====STRING DENGAN BACK SLASH========')
data = "c:\\user\\data\\mull"
print(data)

print('\n=====STRING DENGAN TAB========')
data = "nama saya\t Mull"
print(data)
print(" string dengan tab 1 kali :")

print('\n=====STRING DENGAN TAB 2========')
data = "nama saya\t\t Mull Al-gibrhani"
print(data)
print(" string dengan tab 2 kali :")

print('\n=====STRING DENGAN BACK SPACE========')
data = "nama\b saya\t\t Mull \bAgibrhani"
print(data)
print(" string dengan back space :")

print('\n=====STRING DENGAN NEW LINE========')
data = "nama \t\t: musliadi \njenis kelamin \t: laki-laki"
print(data)
print("string dengan new line atau enter :")

# LF -> line feed -> dipakai oleh unix, macos, linus
print("baris pertama.\nbaris kedua.")

# CR -> cariege return -> dipakai oleh commodore, acorn, lisp
print("baris ketiga.\rbaris keempat.")

# CRLF -> line feed cariege return -> dipakai oleh windows
print("baris kelima.\r\nbaris keenam.")

print('\n=====STRING DENGAN LITERAL ATAU RAW========')
print("C:\new folder")
# menggunakan raw string
print(r"C:\new folder")
print(r"C:\new \r\b\tfolder")

# menggunakan multi line literal string
print("""
1. ini line pertama
2. ini laine kedua
""")
print("""
1. ini line ketiga
2. ini laine keempat
""")

# menggabungkan raw string dan multi line literal string
print(r"""
1. ini line ketiga \b
2. ini laine\n \b \t keempat
""")

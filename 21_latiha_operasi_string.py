userinput = input('masukkan kata : ')
to_upper = userinput.upper()
to_lower = userinput.lower()
di_encode = userinput.encode()
print('ini adalah case normal :', userinput)
print('ini adalah case to upper :', to_upper)
print('ini adalah case to lower :', to_lower)
print('ini adalah case to encode :', di_encode)
txt = "My name is Ståle"
print(txt.encode(encoding="ascii", errors="backslashreplace"))
print(txt.encode(encoding="ascii", errors="ignore"))
print(txt.encode(encoding="ascii", errors="namereplace"))
print(txt.encode(encoding="ascii", errors="replace"))
print(txt.encode(encoding="ascii", errors="xmlcharrefreplace"))

# melakukan pencarian index pada string
txt = "Hello, welcome to my world."
x = txt.find("to")
print(x)

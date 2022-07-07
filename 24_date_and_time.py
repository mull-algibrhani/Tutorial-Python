# import datetime as data_time
# import pytz
# import datetime
from tzlocal import get_localzone
import pytz
from datetime import datetime
from datetime import date
# from datetime import datetime, timezone
# YYYY-MM-DD[*HH[:MM[:SS[.fff[fff]]]][+HH:MM[:SS[.ffffff]]]]
print("\n"+5*"=" + " DATE AND TIME " + 5*"="+"\n")
print(+5*"=" + " Format Date Time " + 5*"=")
waktu_hari_ini = datetime.today()
print("Time Hari ini : ", waktu_hari_ini)
print(f"Hari, ini : {waktu_hari_ini:%A}")
print(f"TBT Hari ini : {waktu_hari_ini:%D}")
print(f"Tgl Hari ini : {waktu_hari_ini:%d}")
print(f"Bulan Hari ini : {waktu_hari_ini:%m}")
print(f"Bulan Hari ini : {waktu_hari_ini:%B}")
print(f"Bulan Hari ini : {waktu_hari_ini:%b}")
print(f"Tahun Hari ini : {waktu_hari_ini:%Y}")
print(f"Tahun Hari ini : {waktu_hari_ini:%y}")
print(f"Jam Hari ini : {waktu_hari_ini:%H}")
print(f"Menit Hari ini : {waktu_hari_ini:%M}")
print(f"Detik Hari ini : {waktu_hari_ini:%S}\n")

print("\n"+5*"=" + " Format Tanggal Lahir " + 5*"="+"\n")
tgl_lahir = date(1994, 5, 4)
print(f"Tgl Lahir : {tgl_lahir:%d}")
print(f"Bln Lahir : {tgl_lahir:%B}")
print(f"Bln Lahir : {tgl_lahir:%Y}")

print("Masukkan Tanggal Lahir")
tanggal = int(input("Masukkan Tanggal \t: "))
bulan = int(input("Masukkan Bulan \t\t: "))
tahun = int(input("Masukkan Tahun \t\t: "))
lahir = date(tahun, bulan, tanggal)
# print(type(tanggal), bulan, tahun)
print("tanggal lahir  anda= ", lahir)
print(f"Harinya adalah = {lahir:%A}")
hari_ini = date.today()
umur_hari = hari_ini - lahir
umur_tahun = umur_hari.days / 365
umur_bulan_sisa = (umur_hari.days % 365) // 30
print("umur dalam hari = ", umur_hari.days, "Hari")
print("umur dalam tahun = ", int(umur_tahun),
      "Tahun", umur_bulan_sisa, "bulan")
# print(umur_bulan_sisa, "Bulan lagi kamu ulang tahun yang ke", int(umur_tahun + 1))
print("\n")

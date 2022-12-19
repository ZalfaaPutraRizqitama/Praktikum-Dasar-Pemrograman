print("========================JOKI.GLOX=========================")
print("Selamat Datang Di JOKI.GLOX")
print("        Tempat Joki Termurah Se Planet Bekasi")
print("Berikut Cara Order :")
print("1. Lengkapi Data Akun Yang Ingin Di Joki")
print("2. Masukkan Nomor HP")
print("3. Masukkan Jumlah Bintang Yang Dipesan")
print("4. Bayarlah Pesanan Yang Telah Anda Buat")
print("5. Orderan Joki Akan Segera Diproses")
print("   Setelah Anda Sudah Membayar")

print("======================LENGKAPI DATA=======================")
import time

Tanggal = time.strftime ("%d-%m-%y - %H:%M:%S")
print(Tanggal)

Pembeli = input ("Nama Pembeli : ") 
Alamat = input("Masukkan Alamat Email Akun Anda :")
Password = input("Masukkan Password :")
ID_dan_Nick = input("Masukkan ID dan Nick Akun Anda :")
Nomor_HP = input("Masukkan Nomor HP Anda :")

def joki():
    global totaljoki
    global jumlahbintang
    global joki
    print("\n=======================DAFTAR JOKI========================")
    print("Dibawah Ini Adalah Daftar Joki Untuk Per Bintang / Win")
    print("1. Epic - Rp.5000,00")
    print("2. Legend - Rp.7000,00")
    print("3. Mythic - Rp.9000,00")
    nomor = int(input("Opsi Yang Anda Pesan : "))
    jumlahbintang = int(input("Berapa Pesanan Joki : "))

    if nomor == 1:
        totaljoki = jumlahbintang * 5000
        print(jumlahbintang, 'Bintang = Rp.' , totaljoki)
        joki=("Bintang")
    elif nomor == 2:
        totaljoki = jumlahbintang * 7000
        print(jumlahbintang, 'Bintang = Rp.' , totaljoki)
        joki=("Bintang")
    elif nomor == 3:
        totaljoki = jumlahbintang * 9000
        print(jumlahbintang, 'Win = Rp.' , totaljoki)
        joki=("Win")
    else:
        print("Pesanan joki tidak ada di daftar menu\nSilahkan pilih kembali!")
        joki()

joki()
total_semua = totaljoki

print("\nTotal yang harus dibayar : " ,total_semua)
uang = int(input("Uang Tunai Pembeli : Rp."))
kembalian = int(uang - total_semua)
print("Kembalian :", kembalian)
print("\n=======================STRUK PESANAN======================")
print("Tanggal\t\t:",Tanggal)
print("Nama\t\t:",Pembeli)
print("Email\t\t:",Alamat)
print("Nomor HP\t:",Nomor_HP)
print("Beli\t\t:",jumlahbintang,joki,"(Rp.{})".format(totaljoki))
print("Tagihan\t\t: Rp.",total_semua)
print("Dibayar\t\t: Rp.",uang)
print("Kembalian\t: Rp.",kembalian)

print("==========================================================")
print("==========================================================")
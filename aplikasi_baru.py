# PROGRAM DASHBOARD
    # tampilan awal suatu website sederhana yang terdiri dari fitur login, create account, help, quit
# KAMUS
    # Variabel
        # aksi : integer { pilihan tindakan yang dilakukan user }
        # flag_end_program : integer { = 1 : menandakan program telah selesai}
# ALGORITMA UTAMA

flag_end_program = 0
# langkah 1 : menyambut user dengan pesan selamat datang
print("Selamat Datang di Crypto")
# langkah 2 : menampilkan opsi yang dilakukan user
print("""
Pilihan Aksi :
(1) login
(2) create account
(3) help
(4) quit
""")

help = """----------------------------------
Anda berada pada menu help
Masukkan aksi berdasarkan pilihan yang ada.

Pilihan Aksi :
(1) login
(2) create account
(3) help
(4) quit

contoh : 
Masukkan aksi:
>>> 1
*login*
----------------------------------
"""

while(flag_end_program == 0):
    # langkah 3 : user akan memilih apa yang ingin dilakukan
    print("Masukkan input:",end="\n>>> ") # prompt input
    aksi = int(input())

    # kasus 1 : user memilih (1) login
    if (aksi == 1):
        # fitur login
        print("ini adalah fitur login")

    # kasus 2 : user memilih (2) create account
    elif (aksi == 2):
        # fitur buat akun
        print("nanti kita kerjakan") # PR buat mas udin
            
    # kasus 3 : user memilih (3) menampilkan pesan help
    elif (aksi == 3):
        # print("fitur menampilkan bantuan")
        print(help)

    # kasus 4 : user memilih (4) user keluar program
    elif (aksi == 4):
        print("selesai")
        flag_end_program = 1
        # keluar program
    else:
        print("opsi aksi tidak ada!")

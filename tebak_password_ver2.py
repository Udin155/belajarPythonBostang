# PROGRAM LOGIN (while loop)
    # user memasukkan id dan password untuk masuk ke suatu website
    # update log : ada id, ada konfirmasi password
# KAMUS
    # Variabel
        # password : integer { password yang tersimpan di database }
        # id : integer { id yang tersimpan di database }
        # flag : integer { penanda program sudah berakhir/belum }
        # tebakan : integer { input dari user untuk }
# ALGORITMA UTAMA

# mendeklarasikan password
password = "123"

# mendeklarsikan id
id = "udin"

# mendeklarasikan flag program
flag = 0 # menandakan apakah program sudah selesai atau belum

flag_id = 0 # menandakan id sudah tepat ditebak, tetapi password masih salah

flag_pw = 0 # menandakan id U sudah benar
while(flag == 0):
    # proses memasukkan id
    print("Masukkan ID", end ="\n>>> ") # \n : artinya baris baru
    tebakan = input()
    if tebakan == id:
        # print("SELAMAT ANDA BERHASIL MEMBOBOL PROGRAM")
        while (flag_id == 0):
            # proses memasukkan password pertama kali
            print("Masukkan password", end ="\n>>> ") # \n : artinya baris baru
            tebakan = input()
            if tebakan == password:
                while (flag_pw == 0):
                    # proses memasukkan password kedua kali (verifikasi)
                    print("konfirmasi password", end ="\n>>> ") # \n : artinya baris baru
                    tebakan = input()
                    if tebakan == password:
                        flag_pw = 1
                        flag_id = 1
                        flag = 1
                        print("selamat kontol lu bisa login")
                    else:
                        print("password tidak sama!")
            else:
                print("SALAH!  COBA LAGI")
    else: 
          # kalau tebakan id salah
          print("Tebakan ID masih salah!")


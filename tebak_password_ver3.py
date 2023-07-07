# PROGRAM LOGIN (while loop)
    # user memasukkan id dan password untuk masuk ke suatu website
    # update log : maksimal tebakan password 3 kali
# KAMUS
    # Variabel
        # password : integer { password yang tersimpan di database }
        # id : integer { id yang tersimpan di database }
        # flag : integer { penanda program sudah berakhir/belum }
        # flag_id : integer { menyatakan password sudah ditebak atau belum }
        # tebakan : integer { input dari user untuk }
        # n_tebak_password : integer { jumlah tebakan yang sudah dilakukan }
# ALGORITMA UTAMA

# deklarasi variabel yang menyatakan sudah berapa kali menebak password
n_tebak_password = 0

# mendeklarasikan password
password = "123"

# mendeklarsikan id
id = "udin"

# mendeklarasikan flag program
flag = 0 # menandakan apakah program sudah selesai atau belum
flag_id = 0 # menandakan id sudah tepat ditebak, tetapi password masih salah    

while(flag == 0):
    # proses memasukkan id
    print("Masukkan ID", end ="\n>>> ") # \n : artinya baris baru
    tebakan = input()

    if tebakan == id:
        # print("SELAMAT ANDA BERHASIL MEMBOBOL PROGRAM")
        flag_id = 0 # menandakan id sudah tepat ditebak, tetapi password masih salah    
        while (flag_id == 0):
            # proses memasukkan password
            print("Masukkan password", end ="\n>>> ") # \n : artinya baris baru
            tebakan = input()
            if (tebakan == password) and (n_tebak_password < 3):
                print("selamat anda berhasil masuk")
                flag_id = 1
                flag = 1
            elif (tebakan != password) and (n_tebak_password < 3):
                print("SALAH!  COBA LAGI")
                # n_tebak_password = n_tebak_password + 1
                n_tebak_password += 1
                print("attempt : {}/3".format(n_tebak_password))        

                # menampilkan sudah berapa kali menebak
                print("anda sudah salah {} kali".format(n_tebak_password))
            # elif n_tebak_password >= 3:
            else:
                print("password salah lebih dari 3 kali!")
                n_tebak_password = 1
                flag_id = 1
                #continue
    else: 
          # kalau tebakan id salah
          print("Tebakan ID masih salah!")
    
    # bagian program setelah login
    print("selamat datang di menu awal")
          

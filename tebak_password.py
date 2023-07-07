password = "pythonEZ"

flag = 0 # menandakan apakah program sudah selesai atau belum

while(flag == 0):
    print("Masukkan password", end ="\n>>> ")
    tebakan = input()
    if tebakan == password:
        print("SELAMAT ANDA BERHASIL MEMBOBOL PROGRAM")
        flag = 1
    else:
        print("SALAH!  COBA LAGI")

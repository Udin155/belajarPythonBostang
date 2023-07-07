# Program remedial
    # akan diberikan kumpulan nama siswa beserta nilainya dalam bentuk array
# kemudian akan dicetak nama siswa yang remedial (nilainya dibawah atau pas kkm) dan mencetak siswa yang nilainya 100 karena diduga mencontek

# KAMUS
# Variabel
# arr_siswa : array[0..6] of string
# arr_nilai : array[0..6] of integer
# kkm : integer

# ALGORITMA UTAMA

# deklarasi variabel
arr_siswa = ["Erik", "Udin", "William", "Ikhsan", "Bostang", "Bram", "Ridho"]
arr_nilai = [50, 80, 90, 95, 70, 100, 85]
n_siswa = 7
kkm = 70

# mencetak siswa yang nilainya dibawah kkm

for k in range(n_siswa-1):
    if ((arr_nilai[k] <= 70) or (arr_nilai[k] == 100)):
        print(arr_siswa[k])
    

# air putih   jus   air putih or jus 
# 0   0    0
# 0   1    1
# 1   0    1
# 1   1    1

# x ^ y
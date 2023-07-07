# Program Bensin
    # user akan punya uang ..., kemudian user memilih jenis bensin serta jumlah liter
    # atau banyaknya (rupiah), kemudian akan dicetak berapa kembaliannya
# KAMUS
    # Variabel
# input_liter : integer
# output_liter : integer
# harga_total : integer { berapa uang yang harus dibayarkan untuk bensin yang spesifik }
# uang : integer { input uang dari user }
# kembalian : integer
# mode_pengisian : integer { 0 : isi berdasarkan bensin, 1 : isi berdasarkan uang }
# jenis_bensin : integer

# ALGORITMA UTAMA

# fungsi
# 
# array -> kumpulan dari variabel

# DEKLARASI VARIABEL
nama_besin = ["premium", "pertalite", "pertamax", "pertamax turbo"]
harga_per_liter = [8000, 10000, 13000, 18000] 

# Langkah 1 : mau input berdasarkan liter atau berdasarkan uang
print("Jenis input:\n0 : isi berapa liter\n1 : isi berapa ribu")
print("mau isi berapa liter? atau berapa ribu?")
mode_pengisian = int(input())

# menentukan jenis BBM
# jenis_besin :: 0 : premium, 1 : pertalite, dst. (sesuai array)
print("0 : premium\n1 : pertalite\n2 : pertamax\n3 : pertamax turbo")
print("mau BBM apa?",end="\n>>> ")

jenis_bensin = int(input())


if (mode_pengisian == 0):

    # mengisi berdasarkan berapa liter yang dimau
    print("Berapa liter mas?",end="\n>>> ")
    input_liter = int(input())

    # menghitung berapa yang harus kita bayar dan berapa kembaliannya
    harga_total = input_liter * harga_per_liter[jenis_bensin]
    print(harga_total)

elif (mode_pengisian == 1):
    # menerima input berapa uang yang diserahkan
    print("mau ngisi berapa ribu, mas?",end="\n>>> ")
    harga_total = int(input())
    # menghitung serta menampilkan berapa liter bensin yang diperoleh
    output_liter = harga_total / harga_per_liter[jenis_bensin]
    print(f"anda mendapat {output_liter:.2f} liter, mas..")

# meminta uang dari user
print("uangnya berapa, mas?",end="\n>>> ")
uang = int(input())

# menentukan kembalian dari user
if (uang < harga_total):
    print("uangnya kurang maseh..")
else:
    kembalian = uang - harga_total
    print(f"kembaliannya sebanyak {kembalian}, mas..")



# Catatan :
# penyederhanaan program
# if (...):
#     aksi_a
#     ...
#     aksi_x
#     aksi_y

# elif (...):
#     aksi_a
#     ...
#     aksi_y


# aksi_a
# if (...):
 
#     ...
#     aksi_x

# elif (...):
#     ...
# aksi_y


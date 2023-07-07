# Program genap
    # akan mencetak bilangan genap dari 1 sampai dengan input user
# KAMUS
    # Variabel
        # x : integer { batas atas dari bilangan genap yang ingin cetak, x >= 0 }
        # arr : array [0..x-1] of integer
# ALGORITMA UTAMA

# langkah 1 : meminta input dari user
print("masukkan input\n>>>")
x = int(input())

# langkah 2 : mencetak bilangan genap dari 1 sampai dengan input user
arr = range(x+1)  # arr = [0,1,2,3,..., x]

for angka in arr:
    if (angka % 2 == 0):
        print(angka)

# genap : 2, 4, 6, --> habis dibagi 2
# habis dibagi : %

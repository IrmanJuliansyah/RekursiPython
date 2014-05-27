def menu():
    pilihan = int(input("Pilih Menu : \n\n1.Fibonacci\n2.Faktorial\n3.Exit \nMasukkan Pilihan Anda [1-3] : "))
    if pilihan == 1:
        nilai = int(input("Masukkan sebuah bilangan : " ))
        hasil = fibonacci(nilai)
        print ("Fibonacci (%d) = %d " % (nilai,hasil))
        kembali()
    elif pilihan == 2:
        cetak=int(input("Masukkan Sebuah Bilangan : "))
        for i in range(cetak+1):
            print ("%2d ! = %d" % (i, faktorial(i)))
        kembali()
    else:
        exit

def fibonacci(n):
    if n < 0:
        print ("Tidak ada bilangan yang bernilai negatif")
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2) 


def faktorial(nilai):
    if nilai <= 1:
        return 1
    else:
        return nilai * faktorial(nilai - 1)

def kembali():
    ulang = input("Ingin mengulang lagi Y/N = ")
    if ulang ==("Y") or ulang ==("y"):
        menu()
    else:
        exit
menu()


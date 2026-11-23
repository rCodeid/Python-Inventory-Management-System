print("===== MANAJEMEN STOK GUDANG =====")
import datetime
barang=int(input("stok barang saat ini : "))
tanggal_gudang=input("masukkan tanggal (YYYYMMDD) :  ")
tanggal=datetime.datetime.strptime(tanggal_gudang , "%Y%m%d").date()

while True:

    print("==== MENU ====")
    print("1. Tambah stok")
    print("2. Kurangi stok")
    print("3. Lihat stok")
    print("4. Keluar")

    pilih=input("Pilih menu : ")

    if pilih == "4":
        print("Anda Keluar")
        break

    elif pilih == "1":
        tambah_barang=int(input("tambahkan stok barang : "))
        barang += tambah_barang
        print("stok ditambah" , barang)

    elif pilih== "2":
        kurang_barang=int(input("kurangi stok barang : "))
        barang -=kurang_barang
        print("stok dikurang" , barang)
      
    elif pilih == "3":
        print("stok saat ini", barang)

    else:
     print("Menu", pilih, "tidak tersedia!")
     continue

    print("========== BARANG ==========")
    print(f"{'barang saat ini':<15} : {barang}")
    print(f"{'tanggal':<15} : {tanggal}")
    print(f"{'menu':<15} : {pilih}")
    break
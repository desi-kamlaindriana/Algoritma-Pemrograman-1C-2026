print("====== Plylist Musik ======")

Plylist_musik = {}
while True:
    Pilih = input('Pilih (buat plylist/tambah lagu/tampilkan/cari lagu/hapus lagu/hapus plylist/keluar) : ').lower()

    if Pilih == "buat plylist":
        Buat_plylist = input("Buat plylist : ")
        Plylist_musik[Buat_plylist] = {}       #temapt lagu lagu
    elif Pilih == "tambah lagu":
        Nama_plylist = input("Nama plylist: ")
        if Nama_plylist in Plylist_musik:       #cek plylist ada tidaknya
            Judul_lagu = input("Judul lagu: ") 
            Penyanyi = input("Penyanyi: ")
            Plylist_musik[Nama_plylist][Judul_lagu] = Penyanyi          #place menambah lagu, key judul lagu valuenya penyanyi
        else:
            print("Plylist tidak ditemukan, silakan buat plylist")
    elif Pilih == 'tampilkan':
        if len(Plylist_musik) == 0:
            print("Belum ada plylist")
        else:
           for (Nama_plylist, Daftar_lagu) in Plylist_musik.items():        #membngkr setiap elemen menjdi 2 key and value
                print(f"Nama plylist: {Nama_plylist}, Daftar lagu: {Daftar_lagu}")

    elif Pilih == 'cari lagu':
        Judul_lagu = input("Judul lagu: ")
        for (Nama_plylist, Daftar_lagu) in Plylist_musik.items():
            if Judul_lagu in Daftar_lagu:
                print(f"Nama plylist: {Nama_plylist}, Judul lagu: {Judul_lagu}, Penyanyi: {Daftar_lagu[Judul_lagu]}")
                break
        else:
            print("Lagu tidak ditemukan")

    elif Pilih == 'hapus lagu':
        Nama_plylist = input("Nama plylist: ")
        Judul_lagu = input("Judul lagu: ")
        for (Plylist, Daftar_lagu) in Plylist_musik.items():
            if Plylist == Nama_plylist and Judul_lagu in Daftar_lagu:       #cek plylist dan lagu ada
                Daftar_lagu.pop(Judul_lagu)      #menhapus lagu di dict daftar lgu
                print("Lagu berhasil dihapus")
                break       #mnghentikan pencarian
        else:
            print("Lagu tidak ditemukan")
    elif Pilih == 'hapus plylist':
        Nama_plylist = input("Nama plylist: ")
        if Nama_plylist in Plylist_musik:
            Plylist_musik.pop(Nama_plylist)
            print("Plylist berhasil dihapus")
        else:
            print("Plylist tidak ditemukan")
    elif Pilih == 'keluar':
        print("Program selesai, thanks")
        break
    else:
        print("Pilihan menu tidak valid")
       
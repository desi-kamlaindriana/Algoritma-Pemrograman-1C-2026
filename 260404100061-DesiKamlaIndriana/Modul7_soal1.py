print("===== To-do list Tugas =====")

Daftar_tugas = {}

while True:
    Pilih = input('Pilih (tambah/tampilkan/tandai/hapus/jumlah/keluar) : ').lower()
    if Pilih == "tambah":
        Tambah_tugas = input("Tambah tugas: ")
        Daftar_tugas[Tambah_tugas] = 'Belum selesai'
    elif Pilih == "tampilkan":
        if len(Daftar_tugas) == 0:
            print("Belum ada tugas")
        else:
            for (tugas, status) in Daftar_tugas.items():       #butuh tugas&status items sekaligus 22
                print(f"Nama tugas: {tugas}, Status: {status}")
    elif Pilih == "tandai":
        Nama_tugas = input("Nama tugas: ")
        if Nama_tugas in Daftar_tugas:
            Daftar_tugas[Nama_tugas] = 'Selesai'
        else:
            print("Tugas tidak ditemukan")
    elif Pilih == "hapus":
        Nama_tugas = input("Nama tugas: ")
        if Nama_tugas in Daftar_tugas:
            Daftar_tugas.pop(Nama_tugas)
            print("Tugas berhasil dihapus")
        else:
            print("Tugas tidak ditemukan")
    elif Pilih == "jumlah":
        Jumlah_tugas_selesai = 0
        Jumlah_tugas_belum = 0
        for (status) in Daftar_tugas.values():     #fokus dfatrs tugas
            if status == 'Selesai':
                Jumlah_tugas_selesai = Jumlah_tugas_selesai + 1
            else:
                Jumlah_tugas_belum = Jumlah_tugas_belum + 1

        print(f"Jumlah_tugas_selesai: {Jumlah_tugas_selesai}")
        print(f"Jumlah tugas belum: {Jumlah_tugas_belum}")
    elif Pilih == 'keluar':
        print("Program selesai, thanks")
        break
    else:
        print("Pilihan menu tidak valid, silakan coba lagi")
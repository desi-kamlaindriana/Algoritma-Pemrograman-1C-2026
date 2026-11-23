print("====== Peserta Webinar ======")

Daftar_undangan = set()
Daftar_Peserta_WebinarA = set()
Daftar_Peserta_WebinarB = set()

Daftar_undangan.update(input('Nama undangan: ').split(','))
Daftar_Peserta_WebinarA.update(input('Peserta webinar A: ').split(','))       #3menambah dan memisah
Daftar_Peserta_WebinarB.update(input('Peserts webinar B: ').split(','))

A = Daftar_Peserta_WebinarA.union(Daftar_Peserta_WebinarB)      #gabungan
print("Semua peserta webinar: ", A)

B = Daftar_Peserta_WebinarA.intersection(Daftar_Peserta_WebinarB)       #irisan
print("Peserta hadir kedua webinar: ", B)

C = Daftar_Peserta_WebinarA.symmetric_difference(Daftar_Peserta_WebinarB)       #selisih beda setankup
print("Peserta hanya hadir salah satu webinar: ", C)

D = Daftar_undangan.difference(A)               #selisih
print("Undangan yang tidak hadir: ", D)

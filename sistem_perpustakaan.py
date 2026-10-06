# ==============================================================
#  PROGRAM  : SISTEM PERPUSTAKAAN MINI
#  MATERI   : Modul 1 (variabel, tipe data, array/list)
#             Modul 2 (pengkondisian)
#             Modul 3 (perulangan)
#             Modul 4 (function dan method)
# ==============================================================

# ---------- MODUL 1: VARIABEL & TIPE DATA ----------
NAMA_PERPUSTAKAAN = "Perpustakaan 51"   # str
VERSI_PROGRAM = 1.0                         # float
DENDA_PER_HARI = 1500                       # int
PERPUSTAKAAN_BUKA = True                    # bool


# ==============================================================
#  BAGIAN 1 : FUNCTION
# ==============================================================

# FUNCTION - NON-RETURN, TANPA PARAMETER
def tampilkan_menu():
    print("\n" + "=" * 40)
    print("              MENU UTAMA")
    print("=" * 40)
    print("1. Tambah buku")
    print("2. Lihat semua buku")
    print("3. Cari buku")
    print("4. Pinjam buku")
    print("5. Kembalikan buku")
    print("6. Total stok & hitung denda")
    print("7. Keluar")
    print("=" * 40)


# FUNCTION - NON-RETURN, BERPARAMETER
def cetak_judul(teks):
    print("\n--- " + teks.upper() + " ---")


# FUNCTION - RETURN, TANPA PARAMETER
def minta_pilihan():
    # Perulangan sampai pengguna memasukkan pilihan yang valid (1-7)
    while True:
        masukan = input("Pilih menu (1-7): ")
        if masukan.isdigit() and 1 <= int(masukan) <= 7:
            return int(masukan)
        print("Input tidak valid! Masukkan angka 1 sampai 7.")


# FUNCTION - RETURN, BERPARAMETER
def cek_status_stok(stok):
    if stok == 0:
        return "Habis"
    elif stok <= 2:
        return "Hampir habis"
    else:
        return "Tersedia"


# FUNCTION - RETURN, BERPARAMETER
def hitung_denda(hari_telat):
    if hari_telat <= 0:
        return 0
    return hari_telat * DENDA_PER_HARI


# ==============================================================
#  BAGIAN 2 : CLASS DAN METHOD
# ==============================================================
class Perpustakaan:

    # Constructor (method non-return)
    def __init__(self, nama):
        self.nama = nama
        # MODUL 1: array / list
        self.judul = []
        self.penulis = []
        self.stok = []
        self.stok_awal = []

    # METHOD - NON-RETURN, BERPARAMETER
    def tambah_buku(self, judul, penulis, stok):
        self.judul.append(judul)
        self.penulis.append(penulis)
        self.stok.append(stok)
        self.stok_awal.append(stok)

    # METHOD - NON-RETURN, TANPA PARAMETER
    def tampilkan_semua(self):
        if len(self.judul) == 0:
            print("Belum ada buku di perpustakaan.")
        else:
            print(f"{'No':<4}{'Judul':<28}{'Penulis':<18}{'Stok':<6}Status")
            print("-" * 70)
            # MODUL 3: perulangan for
            for i in range(len(self.judul)):
                status = cek_status_stok(self.stok[i])
                print(f"{i + 1:<4}{self.judul[i]:<28}{self.penulis[i]:<18}"
                      f"{self.stok[i]:<6}{status}")

    # METHOD - RETURN, TANPA PARAMETER
    def hitung_total_stok(self):
        total = 0
        for jumlah in self.stok:
            total += jumlah
        return total

    # METHOD - RETURN, BERPARAMETER
    def cari_buku(self, judul_dicari):
        for i in range(len(self.judul)):
            if self.judul[i].lower() == judul_dicari.lower():
                return i          # mengembalikan posisi (index) buku
        return -1                 # -1 artinya tidak ditemukan

    # METHOD - NON-RETURN, BERPARAMETER
    def pinjam_buku(self, judul_dicari):
        posisi = self.cari_buku(judul_dicari)
        if posisi == -1:
            print("Buku tidak ditemukan.")
        elif self.stok[posisi] == 0:
            print("Maaf, stok buku sedang habis.")
        else:
            self.stok[posisi] -= 1
            print(f"Berhasil meminjam '{self.judul[posisi]}'. "
                  f"Sisa stok: {self.stok[posisi]}")

    # METHOD - NON-RETURN, BERPARAMETER
    def kembalikan_buku(self, judul_dicari):
        posisi = self.cari_buku(judul_dicari)
        if posisi == -1:
            print("Buku tidak ditemukan.")
        elif self.stok[posisi] >= self.stok_awal[posisi]:
            print("Semua buku ini sudah ada di perpustakaan.")
        else:
            self.stok[posisi] += 1
            print(f"Terima kasih, '{self.judul[posisi]}' telah dikembalikan.")


# ==============================================================
#  BAGIAN 3 : PROGRAM UTAMA
# ==============================================================
def main():
    if not PERPUSTAKAAN_BUKA:
        print("Perpustakaan sedang tutup.")
        return

    perpus = Perpustakaan(NAMA_PERPUSTAKAAN)

    # Data awal
    perpus.tambah_buku("Laskar Pelangi", "Andrea Hirata", 3)
    perpus.tambah_buku("Bumi Manusia", "Pramoedya A.T.", 2)
    perpus.tambah_buku("Negeri 5 Menara", "Ahmad Fuadi", 1)

    print(f"Selamat datang di {perpus.nama} (v{VERSI_PROGRAM})")

    jalan = True
    while jalan:
        tampilkan_menu()
        pilihan = minta_pilihan()

        if pilihan == 1:
            cetak_judul("Tambah Buku")
            judul = input("Judul buku   : ")
            penulis = input("Penulis      : ")
            stok = input("Jumlah stok  : ")
            if stok.isdigit() and judul != "" and penulis != "":
                perpus.tambah_buku(judul, penulis, int(stok))
                print("Buku berhasil ditambahkan!")
            else:
                print("Data tidak valid, buku batal ditambahkan.")

        elif pilihan == 2:
            cetak_judul("Daftar Buku")
            perpus.tampilkan_semua()

        elif pilihan == 3:
            cetak_judul("Cari Buku")
            judul = input("Masukkan judul buku: ")
            posisi = perpus.cari_buku(judul)
            if posisi == -1:
                print("Buku tidak ditemukan.")
            else:
                print(f"Ditemukan: {perpus.judul[posisi]} "
                      f"oleh {perpus.penulis[posisi]} "
                      f"(stok: {perpus.stok[posisi]})")

        elif pilihan == 4:
            cetak_judul("Pinjam Buku")
            judul = input("Judul buku yang dipinjam: ")
            perpus.pinjam_buku(judul)

        elif pilihan == 5:
            cetak_judul("Kembalikan Buku")
            judul = input("Judul buku yang dikembalikan: ")
            perpus.kembalikan_buku(judul)

        elif pilihan == 6:
            cetak_judul("Total Stok & Denda")
            print("Total seluruh stok buku:", perpus.hitung_total_stok())
            hari = input("Berapa hari keterlambatan? ")
            if hari.isdigit():
                denda = hitung_denda(int(hari))
                print(f"Denda yang harus dibayar: Rp{denda}")
            else:
                print("Input harus berupa angka.")

        else:
            print("\nTerima kasih telah menggunakan program ini. Sampai jumpa!")
            jalan = False


# Menjalankan program
main()
class KarakterSurfer:
    def __init__(self, nama):
        self.nama = nama
        self.skor = 0
        self.koin = 0
        self.is_running = True

    def berlari(self):
        self.is_running = True
        print(f"{self.nama} mulai berlari!")

    def ambil_koin(self, jumlah):
        self.koin += jumlah
        print(f"{self.nama} mengambil {jumlah} koin. Total koin: {self.koin}")

    def tabrak_rintangan(self):
        self.is_running = False
        print(f"Game over! {self.nama} menabrak rintangan.")

    def info_player(self):
        status = "sedang berlari" if self.is_running else "tidak berlari"
        print(
            f"Nama: {self.nama}\n"
            f"Skor: {self.skor}\n"
            f"Jumlah koin: {self.koin}\n"
            f"Status: {status}"
        )


# --- PENGUJIAN OBJEK ---
player1 = KarakterSurfer("Jake")
player1.info_player()
player1.berlari()
player1.ambil_koin(10)
player1.ambil_koin(25)
player1.ambil_koin(10)
player1.tabrak_rintangan()
player1.info_player()
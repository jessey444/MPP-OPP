class KatakZuma:
    def __init__(self, warna_perluru, skor, is_active):
        self.warna_perluru = warna_perluru
        self.skor = skor=0
        self.is_active = is_active=True

    def ganti_warna(self, warna_baru):
        self.warna_perluru = warna_baru
        print(f"Warna peluru diubah menjadi {self.warna_perluru}")

    def tembak(self):
        self.skor += 50
        print(f"Katak Zuma menembakkan peluru berwarna {self.warna_perluru} dan mendapatkan 50 poin skor.")

    def info_status(self):
        status = "aktif" if self.is_active else "tidak aktif"
        print(f"Katak Zuma berwarna {self.warna_perluru} saat ini {status} dengan skor {self.skor}.")

katak_player = KatakZuma("biru", 0, True)
katak_player.info_status()
katak_player.ganti_warna("merah")
katak_player.tembak()
katak_player.info_status()
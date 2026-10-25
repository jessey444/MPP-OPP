class Tamagoci:
    def __init__(self, nama):
        self.nama = nama
        self.lapar = 50
        self.bahagia = 50

    def makan(self):
        self.lapar = max(0, self.lapar - 20)
        print(f"{self.nama} sudah makan. Tingkat lapar: {self.lapar}")

    def bermain(self):
        self.bahagia = min(100, self.bahagia + 20)
        self.lapar = min(100, self.lapar + 10)
        print(f"{self.nama} bermain dengan senang. Tingkat bahagia: {self.bahagia}")

    def info_hewan(self):
        print(
            f"Nama: {self.nama}\n"
            f"Tingkat lapar: {self.lapar}\n"
            f"Tingkat bahagia: {self.bahagia}"
        )


pet1 = Tamagoci("Mochi")
pet1.info_hewan()
pet1.makan()
pet1.bermain()
pet1.info_hewan()
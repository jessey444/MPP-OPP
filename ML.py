class Commander: # membuat  class
    def __init__(self, nama, role, hp, attack_power, gold): #class construktor
        self.nama = nama
        self.hp = hp
        self.attack_power = attack_power #properties
        self.role = role
        self.gold = gold

    def serang(self, target):
        damage = self.attack_power
        target.terima_dammage(damage)
        print(f" {self.nama} menyerang {target.nama} sebesar {damage} DMG ")

    def terima_damage(self, jumlah):
        self.hp -= jumlah
        if self.hp < 0:
            self.hp = 0

    def masih_hidup(self):
        return self.hp > 0 

    def dapatkan_gold(self, jumlah):
        self.gold += jumlah
        print(f"{self.nama} mendapatkan {jumlah} gold. Total gold: {self.gold}")

k1 = Commander("Commander A", "Tank", 100, 20, 50)
k2 = Commander("Commander B", "DPS", 80, 30, 30)


k1.dapatkan_gold(50)
k2.dapatkan_gold(70)

print(f"{k1.nama} (HP: {k1.hp}, Role: {k1.role}, Gold: {k1.gold})")
print(f"{k2.nama} (HP: {k2.hp}, Role: {k2.role}, Gold: {k2.gold})")
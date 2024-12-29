# Class
class Kapal:
    # Constructor
    def __init__(self, jenis):
        self.Type = ""
        self.Merk = ""
        self.jenis = jenis

    # Method to print ship information
    def printKapal(self):
        print("Jenis Kapal : ", self.Type)
        print("Merk Kapal : ", self.Merk)
        print("Kegunaan : ", self.jenis)
    
    # Method to indicate setting completion
    def selesaiSetting(self, kondisi):
        print("Kapal telah disiapkan untuk digunakan")
        print(kondisi)

# Objects
kapal1 = Kapal("Pengangkut Barang")
kapal2 = Kapal("Penumpang")

# Set values
kapal1.Type = "Kargo"
kapal1.Merk = "Maersk"
kapal2.Type = "Feri"
kapal2.Merk = "Pelni"

# Call methods
kapal2.printKapal()
kapal2.selesaiSetting("Kapal telah lulus uji kelayakan.")

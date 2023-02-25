class Kendaraan:
    def __init__(self, jenisKendaraan) -> str:
        self.jenisKendaraan = jenisKendaraan
        return jenisKendaraan


class RodaDua(Kendaraan):
    def __init__(self, jenisKendaraan):
        super().__init__(jenisKendaraan)
        self.jenisKendaraan = jenisKendaraan


class RodaEmpat(Kendaraan):
    def __init__(self, jenisKendaraan):
        super().__init__(jenisKendaraan)
        self.jenisKendaraan = jenisKendaraan


kendaraanRodaDua = RodaDua('Honda')
print(kendaraanRodaDua.jenisKendaraan)

kendaraanRodaEmpat = RodaEmpat('Toyota')
print(kendaraanRodaEmpat.jenisKendaraan)

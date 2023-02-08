# 1. Buatlah fungsi untuk menghitung total bilangan pada list, tidak boleh pakai built in function
#    input  : list bilangan
#    output : total bilangan (int)

# Jawaban soal 1
def hitungTotalBilangan(bilanganList):
    total = 0
    for bil in bilanganList:
        total += bil

    return total


# 2. Buatlah fungsi untuk menghitung volume balok
#    input : panjang, lebar , tinggi (int)
#    output: volume balok (int)

# Jawaban soal 2

def volumeBalok(panjang, lebar, tinggi):
    return panjang*lebar*tinggi

# 3. Buatlah fungsi untuk mencetak kalimat perkenalan seperti berikut:
#    "Halo, nama saya {} dan saya berasal dari {kota asal}"
#    input  : nama
#    output : print string

# Jawaban soal 3


def perkenalan(nama, kotaAsal):
    return f"Hallo, nama Saya {nama} dan saya berasal dari {kotaAsal}"


# 4. Buatlah fungsi untuk membuat kalimat panjang dari sebuah list
#    input  : list string
#    output : string

# jawaban soal 4
def kalimatPanjang(listKalimat):
    kalimat = ""
    for kata in listKalimat:
        kalimat += kata + " "

    return kalimat

# 5. Buatlah fungsi untuk mencetak bilangan ganjil yang ada pada sebuah list
#    input  : list bilangan
#    output : print list bilangan ganjil

# jawaban soal 5


def cetakBilanganGanjil(listBilanganGanjil):
    bilGanjil = []
    for bil in listBilanganGanjil:
        if (bil % 2 != 0):
            bilGanjil.append(bil)

    return bilGanjil


# ===== Output =====
# 1
listBilangan = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Soal 1 : Total Bilangan adalah ", hitungTotalBilangan(listBilangan))

# 2
panjang = float(10)
lebar = float(8)
tinggi = float(5)

hasil = volumeBalok(panjang, lebar, tinggi)
print("Soal 2 : Volume Balok adalah ", hasil)

# 3
nama = "Budi"
kota = "Salatiga"
print("Soal 3 :", perkenalan(nama, kota))

# 4
kalimat = ["Hallo", "ini", "adalah", "sebuah", "kalimat"]
print("soal 4 :", kalimatPanjang(kalimat))

# 5
angka = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
print("Soal 5 :", cetakBilanganGanjil(angka))

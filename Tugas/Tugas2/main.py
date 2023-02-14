import volume


# 1. Buatlah sebuah fungsi untuk mencari bilangan prima yang ada pada range bilangan tertentu
# input: nilai awal, nilai akhir
# output: list bilangan prima

# Jawaban Soal 1
def hitungBilPrima(awal, akhir):
    bilangan_prima = []
    for angka in range(awal, akhir+1):
        if angka > 1:
            for i in range(2, int(angka**(0.5))+1):
                if (angka % i) == 0:
                    break
            else:
                bilangan_prima.append(angka)
    return bilangan_prima


awal = 1
akhir = 10
print("=== Soal 1 ===")
print(hitungBilPrima(awal, akhir))

# 2. Buatlah fungsi untuk mencari bilangan ganjil pada range bilangan tertentu
# input: nilai awal, nilai akhir
# output: list bilangan ganjil

# Jawaban Soal 2


def bilanganGanjil(awal, akhir):
    bilGanjil = list(range(awal, akhir+1))
    listBilGanjil = []

    for bil in bilGanjil:
        if (bil % 2 != 0):
            listBilGanjil.append(bil)

    return listBilGanjil


awalGanjil = 1
akhirGanjil = 15
print("\n=== Soal 2 ===")
print(bilanganGanjil(awalGanjil, akhirGanjil))

# 3. Buatlah fungsi untuk mencari bilangan prima ganjil pada range bilangan tertentu, gunakan fungsi dari
# soal pertama dan kedua untuk membuat fungsi ini
# input: nilai awal, nilai akhir
# output: list bilangan prima ganjil

# Jawaban soal 3


def hitungBilPrimaGanjil(awal, akhir):
    bilangan_prima = hitungBilPrima(awal, akhir)
    bilangan_prima_ganjil = []
    for angka in bilangan_prima:
        if angka % 2 == 1:
            bilangan_prima_ganjil.append(angka)
    return bilangan_prima_ganjil


awal = 1
akhir = 20
print("\n=== Soal 3 ===")
print(hitungBilPrima(awal, akhir))

# 4. Buatlah fungsi untuk membalikkan karakter pada string
# input: string
# output: string yang telah dibalik
# Contoh: input -> "salatiga", output -> "agitalas"

# Jawaban Soal 4


def soal4(string):
    return string[::-1]


print("\n=== Soal 4 ===")
strKalimat = "salatiga"
print(soal4(strKalimat))


# 5. Buatlah fungsi untuk mengecek apakah suatu string adalah palindrome/tidak, boleh menggunakan fungsi dari soal
# nomor 4 untuk mempermudah dalam membuat fungsi
# input: string
# output: boolean
# Contoh: "kasur rusak"

# Jawaban Soal 5
print("\n=== Soal 5 ===")
strKalimatSoal5 = "kasur rusak"
print(f"Kalimat : {strKalimatSoal5}")
if (strKalimatSoal5 == soal4(strKalimatSoal5)):
    print("Kalimat yang diinputkan termasuk Palindrom")
else:
    print("Kalimat yang diinputkan tidak Palindrom")

# 6. Buatlah fungsi untuk mencari selisih nilai tertinggi dan terendah bilangan pada sebuah list
# input: list bilangan
# output: selisih bilangan tertinggi & terendah

# Jawaban Soal 6


def soal6(list_bilangan):
    max_num = max(list_bilangan)
    min_num = min(list_bilangan)
    selisih = max_num - min_num
    return selisih


listBilanganSoal6 = [5, 6, 3, 10, 12, 16]
print("\n=== Soal 6 ===")
print(f"Selisih bilangan tertinggi dan terendah : {soal6(listBilanganSoal6)}")

# 7. Buatlah fungsi untuk menghitung jumlah huruf vokal dan konsonan yang ada pada sebuah string
# input: string
# output: list/tuple jumlah huruf vokal dan konsonan

# Jawaban Soal 7


def soal7(string):
    vokal = 'aeiouAEIOU'
    jml_vokal = 0
    jml_konsonan = 0

    for huruf in string:
        if huruf in vokal:
            jml_vokal += 1
        elif huruf.isalpha():
            jml_konsonan += 1

    return jml_vokal, jml_konsonan


strSoal7 = "Hallo"
print("\n=== Soal 7 ===")
print(f"Soal 7 : {soal7(strSoal7)}")


# 8. Buatlah fungsi untuk mencari bilangan tertentu beserta indexnya pada sebuah list
# input: list bilangan, bilangan yang dicari
# output: dictionary {'status': boolean status hasil pencarian, 'index': index element}

# Jawaban soal 8
def soal8(list_bilangan, bilangan_cari):
    hasil = {'status': False, 'index': None}

    for i, bilangan in enumerate(list_bilangan):
        if bilangan == bilangan_cari:
            hasil['status'] = True
            hasil['index'] = i
            break

    return hasil


listBilanganSoal8 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
bilanganYangAkanDicari = 5
print("\n=== Soal 8 ===")
print(
    f"Bilangan yang ingin dicari {bilanganYangAkanDicari}, hasil : {soal8(listBilanganSoal8, bilanganYangAkanDicari)}")

# 9. Buatlah fungsi aritmatika dengan 3 parameter(operator, bilangan 1, bilangan 2) dengan default value bilangan
# bernilai 1 yang dapat melakukan operasi penjumlahan, pengurangan, perkalian, dan pembagian
# Pada fungsi tersebut gunakan exception untuk memberi tahu user jika salah ketika memberikan input operator,
# terdapat zero division error, dsb
# input: operator(str), bilangan 1, (int) bilangan 2 (int)
# output: hasil operasi aritmatika

# Jawaban soal 9


def soal9(operator, bilangan1=1, bilangan2=1):
    try:
        if operator == "+":
            hasil = bilangan1 + bilangan2
        elif operator == "-":
            hasil = bilangan1 - bilangan2
        elif operator == "*":
            hasil = bilangan1 * bilangan2
        elif operator == "/":
            hasil = bilangan1 / bilangan2
        else:
            raise ValueError("Operator tidak valid")
    except ZeroDivisionError:
        return "Tidak dapat melakukan pembagian dengan 0"
    except Exception as e:
        return str(e)
    else:
        return hasil


operatorSoal9 = '+'
bil1Soal9 = 5
bil2Soal9 = 7
print("\n=== Soal 9 ===")
print(
    f"Hasil dari {bil1Soal9} {operatorSoal9} {bil2Soal9} : {soal9(operatorSoal9, bil1Soal9, bil2Soal9)}")


# 10. Buatlah modul bernama volume.py, buat fungsi untuk menghitung volume
# kubus, balok, limas segi 4, dan prisma segi 3. Kemudian panggil fungsi" tersebut
# pada main.py

# Jawaban Soal 10
sisi = 5
panjang = 10
lebar = 8
tinggi = 6
alas = 4
tinggi_limas = 7
tinggi_prisma = 9

print("\n=== Soal 10 ===")
print("Hitung Kubus dengan sisi :", sisi,
      ", hasil :", volume.hitungKubus(sisi))

print("Hitung balok dengan panjang :", panjang, ", lebar:", lebar,
      ", dan tinggi:", tinggi, ", hasil : ", volume.hitungBalok(panjang, lebar, tinggi))

print("Hitung limas segiempat dengan alas:", alas, ", tinggi:", tinggi, ", dan tinggi limas:",
      tinggi_limas, ", hasil : ", volume.hitungLimasSegiempat(alas, tinggi, tinggi_limas))

print("Volume prisma segitiga dengan alas:", alas, ", tinggi:", tinggi, ", dan tinggi prisma:",
      tinggi_prisma, ", hasil :", volume.hitungPrismaSegitiga(alas, tinggi, tinggi_prisma))

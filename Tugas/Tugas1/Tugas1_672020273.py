# Stevanus Evan Pangau - 672020273

priceTuple = (10000, 13000, 8000, 9000, 16000)
fruitTuple = ('mangga', 'apel', 'jeruk', 'semangka', 'anggur')

# Soal 1
# Buatlah dictionary dengan nama fruitDict dari kedua tuple di atas sehingga menjadi
# {'mangga': 10000, 'apel': 13000, dst...}

# Jawaban Soal 1
fruitDict = {'mangga' : 10000, 'apel' : 13000, 'jeruk' : 8000, 'semangka' : 9000, 'anggur' : 16000}

print("\nJawaban soal (1 - 2)")
print(fruitDict)

# Soal 2
# Dari dictionary fruitDict yang sudah terbuat, hitunglah rata-rata harga buah

# Jawaban Soal 2
ratarata = 0.0
panjang = len(fruitDict)
for i in fruitDict:
    ratarata += fruitDict[i]/panjang

print(ratarata)

# ==================================================================================

test_list = [4, 1, {'tiga': 3, 'tujuh': 7}, (9, 8, [2, 5]), 6]
# Soal 3
# Dari test_list di atas, buatlah sebuah string dengan isi : '1 2 3 4 5 6 7 8 9'

# Jawaban Soal 3
listTuple = test_list[2]

resultSoal3 = f"{test_list[1]} {test_list[3][2][0]} {listTuple['tiga']} {test_list[0]} {test_list[3][2][1]} {test_list[4]} {listTuple['tujuh']} {test_list[3][1]} {test_list[3][0]}"

print("\nJawaban soal (3 - 4)")
print(resultSoal3)


# Soal 4
# Dari string tersebut pecahlah kembali menjadi sebuah list yang berisi integer, kemudian hitung nilai total dari isi list

# Jawaban Soal 4
resultSoal3Split = resultSoal3.split()
totalListSoal3 = 0
for i in resultSoal3Split:
    totalListSoal3 += int(i)

print(totalListSoal3)

# ==================================================================================

str1 = "teknik informatika fakultas teknologi informasi universitas kristen satya wacana"
str2 = "sedang belajar bahasa pemrograman"
tupleMahasiswa = ('DEVA', 'IVAN')
dictKelas = {'IF001': 'Kapita Selekta', 'IF002': 'Matematika Diskrit', 'IF003': 'Pemrograman Web'}
listPython = ['p', 'y', 't', 'h', 'o', 'n']

# Soal 5
# Dari variable di atas, buatlah string sebagai berikut
# - 'Hari ini Deva tidak mengikuti mata kuliah Pemrograman Web'
# - 'Matematika Diskrit IF002 adalah salah satu mata kuliah di progdi Teknik Informatika Universitas Kristen Satya Wacana'
# - 'Ivan belajar bahasa pemrograman Python di mata kuliah Kapita Selekta'

# Jawaban soal 5
str1Split = str1.split()
str2Split = str2.split()

print("\nJawaban soal (5)")
print(f"Hari ini {tupleMahasiswa[0][0] + tupleMahasiswa[0][1:].lower()} tidak mengikuti mata kuliah {dictKelas['IF003']}")
print(f"{dictKelas['IF002']} {list(dictKelas.keys())[1]} adalah salah satu mata kuliah di progdi {str1Split[0][0:1].upper() + str1Split[0][1:]} {str1Split[1][0:1].upper() + str1Split[1][1:]} {str1Split[5][0:1].upper() + str1Split[5][1:]} {str1Split[6][0:1].upper() + str1Split[6][1:]} {str1Split[7][0:1].upper() + str1Split[7][1:]} {str1Split[8][0:1].upper() + str1Split[8][1:]}")
strPython = ''.join(listPython)
print(f"{tupleMahasiswa[1][0] + tupleMahasiswa[1][1:].lower()} {str2[7:]} {strPython[0].upper() + strPython[1:]} di mata kuliah {dictKelas['IF001']}")

# ==================================================================================

listHari = ['Senin', 'Rabu', 'Jumat', 'Sabtu']
# Soal 6
# Tambahkan hari 'Selasa', 'Kamis', dan 'Minggu', sehingga listHari tersebut menjadi ['Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu', 'Minggu']

# Jawaban Soal 6
listHari.insert(1, "Selasa")
listHari.insert(3, "Kamis")
listHari.append("Minggu")

print("\nJawaban soal (6 - 7)")
print(listHari)

# Soal 7
# Hapus hari 'Sabtu' dan 'Minggu' dari listHari, kemudian copy list listHari ke variable tupleHariKerja dengan tipe data tuple

# Jawaban Soal 7
listHari.remove('Sabtu')
listHari.remove('Minggu')
print(listHari)

tupleHariKerja = tuple(listHari)
print(tupleHariKerja)
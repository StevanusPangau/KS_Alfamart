# 08 Feb 2023
# Function

"""
def namaFungsi(input/parameter):
    <--- blok kode --->
"""

# contoh hanya fungsi yang dijalankan tanpa ada kembalian (return)


def index():
    print("Hello World")

# contoh fungsi return


def contohFungsiReturn():
    return "Ini adalah fungsi return"

# di python dapat mengembalikan nilai sekaligus


def multiOutput():
    return 1, 2, 3


"""
# func 1
index()

# func 2
print(contohFungsiReturn())

# func
output1, output2, output3 = multiOutput()
print("output 1 :", output1)
print(f"output 2 : {output2}")
print("output 3 : " + str(output3))
"""


def fungsi():
    print("Eksekusi print")


# fungsi untuk melihat file mana yang sedang dikerjakan
"""
print("\nFile Yang Sedang Dikerjakan : ", __name__)

if __name__ == "__main__":
    # 1
    index()

    # 2
    print(contohFungsiReturn())

    # 3
    output1, output2, output3 = multiOutput()
    print("output 1 :", output1)
    print(f"output 2 : {output2}")
    print("output 3 : " + str(output3))
"""

# contoh file exception
"""
try:
    contohVarError = 1
    # contohVarError # contoh error
except Exception as error:
    print("Line 68 : ", error)
"""

# Parameter Function global/local
"""
x = 50


def fungsiA(x):
    print("x = ", x)
    x = 2
    print("Merubah lokal variabel x = ", x)


fungsiA(100)
print("nilai x masih %s" % x)


def fungsiDenganKeyword(paramA, paramB, paramC=123, paramD=345):
    print(f"Param A : {paramA}")
    print(f"Param B : {paramB}")
    print(f"Param C : {paramC}")
    print(f"Param D : {paramD}")


fungsiDenganKeyword(1, 2)
print("-------------------------- Manipulasi --------------------------")
# bisa ganti value dari default parameter
fungsiDenganKeyword(1, 2, paramC=321, paramD=543)
fungsiDenganKeyword(1, 2, 777, 888)
"""

"""
x = 50


def fungsi1():
    print("print variabel global x :", x)


def fungsi2():
    x = 100
    print("print variabel local x :", x)


def fungsi3():
    global x
    x = 300
    print("[new] print variabel global", x)


fungsi1()
fungsi2()
fungsi3()
print(x)
"""


def total(*bilangan, **keywords):
    hitung = 0

    for bil in bilangan:
        hitung += bil

    for key in keywords:
        hitung += keywords[key]

    return hitung


print("versi 1 : ", total(1, 2, 3, 4, 5))
print("versi 2 : ", total(daging=2, sayur=10, buah=3))
print("versi 3 : ", total(7, 8, 5, sayur=10, buah=3, daging=2))

# -------------------------- contoh pengunaan kwargs dengan mengambil key/nama paramater


def contohKwargs(**kwargs):
    # kwargs juga
    # 100 dibelakang adalah nilai default bila fungsi "get" tidak dapat menemukan kunci "paramA"
    varParamA = kwargs.get('paramA', 100)
    print(varParamA)


contohKwargs(paramA=200)  # hasilnya 200
contohKwargs()  # hasil 100

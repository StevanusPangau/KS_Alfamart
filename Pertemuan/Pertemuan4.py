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


# contoh file exception
try:
    contohVarError = 1
    # contohVarError # contoh error
except Exception as error:
    print("Line 68 : ", error)

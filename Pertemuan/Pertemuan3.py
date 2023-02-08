# 01 February 2023

# Flow Control

# a = 1
# contoh if else
"""
if a == 1:
    print("a bernilai 1")
elif a == 2:
    print("a bernilai 2")
else:
    print("a bernilai selain 1 dan 2")
"""

# if else logika
"""
if a == 1 or a == 2 and a != 1:
    print("a bernilai 1 atau a bernilai 2")
else:
    print("a bernilai selain 1 dan 2")
"""

# Nested if
"""
if a == 1:
    if a >= 2:
        print("a lebih dari 2")
    else:
        print("a tidak bernilai lebih dari 2")
else:
    print("a bukan int")
"""

# === Looping ===
"""
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
b = ['a', 'b', 'c', 'd', 'f', 'g']
"""

"""
for x in a:
    print(x)
"""
# === nested for ===
"""
for x in a:
    for y in b:
        if x == 2 and y == 'f':
            print("c bernilai 2 dan y bernilai 'f'")
"""

# === range di for ===
# jadi range pada for memiliki 3 parameter yaitu angka awal, angka akhir, angka untuk ditambah (secara default range dimulai dari angka 0)
"""
for x in range(1, 10, 2):
    print(x)
"""

"""
print("Break")
for x in a:
    if x == 5:
        break
        print(f"nilai {x}")
    print(x)

print("\nContinue")
for x in a:
    if x == 5:
        continue
        print(f"nilai {x}")
    print(x)

print("\nPass")
for x in a:
    if x == 5:
        pass
        print(f"nilai {x}")
    print(x)
"""


# Random

# File Handling
"""
# a = [1, 2, 3, 4, 5, 6]
a = ('a', 'b', 'c', 'd')
fopen = open("filetext.txt", "a")
# fopen.write(a)  # untuk menuliskan kata kedalam file
fopen.writelines(a)  # untuk menambahkan kalimat di dalam file text
fopen.close()
"""

# Function
# function dalam python biasa ditulis 'def'

"""
def index(nama="Evan"):  # contoh paramater dengan nilai default
    print(f"Hello World {nama}")

index("Tivani")
"""

# Function dengan kembalian/return

"""
def hello(a, b, c):
    return a, b, c
"""

# variableA = hello(1, 2, 3)
# print(variableA)
# print(variableA[1])

# contoh mengambil nilai dari function return langsung dimasukan kedalam variable
"""
nilaiA, nilaiB, nilaiC, nilaiD = variableA
print(nilaiA)
print(nilaiB)
print(nilaiC)
print(nilaiD)
"""


"""
def indexA():
    print("Hello world A")


def indexB():
    print("Hello world B")


def indexC():
    print("Hello world C")
"""

"""
indexA()
indexB()
indexC()
"""

# ketika tidak main import main tersebut akan di eksekusi. main tersebut seperti main functionnya
# Contoh pemangilan function main ada di file kode.py

"""
if __name__ == "__main__":
    print("hello world main")
    indexA()
    indexB()
    indexC()
"""

# Path

import datetime
print(datetime.datetime.now())

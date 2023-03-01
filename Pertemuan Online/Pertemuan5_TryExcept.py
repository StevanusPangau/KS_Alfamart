# 15 Feb 2023
# Review Exception Hendling (try/except dan raise)

"""
try:
    print("Masuk Try")
except:  # Base Exception
    print("Error")
"""
# -------------------------------------
# Try catch dengan kondisi tertentu
"""
try:
    print("Masuk Try")
except ZeroDivisionError as error_1:
    print("Tidak boleh dibagi dengan 0")
except ValueError as error_2:
    print("Error baru")
except Exception as error:
    print(type(error))  # untuk melihat error apa yang terjadi
    print(error)  # untuk melihat pesan pada error
    # print("Error")
"""
# --------------------------------------
# Try Catch Else
'''
try:
    print("Masuk Try")
except Exception as error:  # Base Exception
    print("Error")
else:
    print("Masuk else")
"""
Else
    Jika program tidak masuk else maka akan dijalankan exception
    Jika program tidak masuk exception maka akan dijalankan else
"""
'''

# --------------------------------------
# Try Catch Finally
'''
try:
    print("Masuk Try")
except Exception as error:
    print("Masuk error")
finally:
    print("Masuk Finally")
"""
Finnaly
    Jika program masuk ke exception atau program tidak masuk ke exception, maka jalankan finally
"""
'''


# RAISE
angka = 0

if angka == 0:
    print("Nilai 0")
    raise Exception("Variable tidak boleh bernilai 0")
else:
    print("Nilai anda : ", str(angka))

# .

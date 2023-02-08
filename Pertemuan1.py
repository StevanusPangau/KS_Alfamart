# PERTEMUAN 1 PENGENALAN PYTHON

# Sample Comment Hello World

# Comment multiline
'''
Ini
Komen
Multiline
'''

a = "tes"
variableA = "Hello World " + a
# print(type(a))
print(variableA)

variableA = 1
stringVariableA = str(variableA)

stringB = "Hello World"

print("Type Variable A", type(variableA))
print("Type Str Variable A", type(stringVariableA))
print("Type String B", type(stringB))

# Sub String
# print("Subtring ", stringB[0:6])

# Memunculkan tulisan hello
variableSubstring = stringB[0:5]
print(variableSubstring)
print("Length ", len(variableSubstring))

# Memunculkan tulisan World
variableSubstringWorld = stringB[6:11]
print(variableSubstringWorld)
print("Length ", len(variableSubstringWorld))

# 15 Feb 2023

# Materi Class
class Person:
    """
    Documentasi:
    Ini adalah class person, digunakan untuk..
    @attribut 
        nama
        umur
    """
    # name = "Evan"

    # Constructor Python
    def __init__(self, name, age, address, student_id):
        self.name = name
        self.age = age
        self.student_id = student_id
        self.__address = address  # contoh atribut private

    def setAddress(self, newAddress):
        self.__address = newAddress
        return self.__address

    # ambil addres dengan getter
    def getAddress(self):
        return self.__address

    # method untuk menghapus class
    """
    def __del__(self):
        print("Person Destroyed")
    """

    def __str__(self) -> str:
        return f"Nama Saya {self.name}, Usia Saya {self.age}"

# Inheritence


class Student(Person):
    def __init__(self, name, age, address, student_id):
        super().__init__(name, age, address, student_id)
        self.student_id = student_id

# print(Person.name)
# print(Person.__name__)  # untuk melihat nama class
# print(Person.__doc__)  # untuk melihat documentasi dari class


# Panggil class dengan function
evan = Person("Evan", 20, "Manado", "001")


print(evan.name)
print(evan.age)
print(evan.setAddress("Salatiga"))
# print(evan.getAddress())
print(evan.student_id)
print(evan)

# memangil class student
# student = Student("siswa", 10, "Student", "002")
# print(student.name)
# print(student.age)
# print(student.getAddress())
# print(student.student_id)

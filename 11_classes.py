# Classes

class MyEmptyPerson:
    pass

print(MyEmptyPerson)
print(MyEmptyPerson())

class Person:
    def __init__(self, name, surname, alias = "Sin alias"):
        self.full_name = f"{name} {surname} {alias}"

    def walk (self):
        print(f"{self.full_name} esta caminando")

my_person = Person("Guido", "Rimati")
print(my_person.full_name)
my_person.walk()

my_other_person = Person("Arturo", "Perro", "Negro")
print(my_other_person.full_name)
my_other_person.walk()
my_other_person.full_name = "Milanesa Olorosa (Vomitadora)"
print(my_other_person.full_name)
my_other_person.walk()
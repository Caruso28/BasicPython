# Functions

def my_function():
    print("Esto es una funcion")
my_function()

def sum_two_values (first_number, second_number):
        print(first_number + second_number)
sum_two_values(5, 7)
sum_two_values(433435, 65657)
sum_two_values(5.3, 7.1)
my_result = sum_two_values(5.3, 7.1)
print(my_result)

def sum_two_values_with_return (first_number, second_number):
        return first_number + second_number
my_result = sum_two_values_with_return (10, 5)
print(my_result)

def print_name (name, surname):
    print(f"{name} {surname}")
print_name(surname = "Rimati", name = "Guido")

def print_name_with_default (name, surname, alias = "Sin alias"):
    print(f"{name} {surname} {alias}")
print_name_with_default(surname = "Rimati", name = "Guido")
print_name_with_default(surname = "Rimati", name = "Guido", alias = "Programador")

def print_upper_texts(*texts):
    for text in texts:
        print (text.upper())
print_upper_texts ("Hola", "Python")
print_upper_texts ("Hola")

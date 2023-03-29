# Variables
my_string_variable = "My string variable"
print(my_string_variable)

my_int_variable = 5
print(my_int_variable)

my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

my_bool_variable = True
print(my_bool_variable)

# Concatenacion de variables en un print
print(my_string_variable, str(my_int_variable), my_bool_variable)

# Funciones del Sistema
# len cuenta los caracteres
print(len(my_string_variable))

# Variables en una sola linea
name, surname, alias, age = "Guido", "Rimati", "Rey", 37
print("Me llamo", name, surname, ", me dicen", alias, "y mi edad es", age)

# Inputs
name = input("¿Cual es tu nombre?")
age = input("¿Cuantos años tienes?")
print(name)
print(age)
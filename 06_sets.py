# Sets

my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set))

my_other_set = {"Guido", "Rimati", 37}
print(type(my_other_set))
print(len(my_other_set))

my_other_set.add("Programador")
print((my_other_set))

# Set no es ordenado (ej alio ordenado de casualidad), no es inmutable, y no acepta elementos repetidos.

# Verificar si un elemento esta en el Set
print("Programador" in my_other_set)
print("Programado" in my_other_set)

# Quitar elementos
my_other_set.remove("Programador")
print((my_other_set))

# Borrar todos los elementos del Set
my_other_set.clear()
print((my_other_set))
print(len(my_other_set))

# Eliminar el Set
del my_other_set
# print((my_other_set))

# Convertir Set en Lista
my_set = {"Guido", "Rimati", 37}
my_list = list(my_set)
print(my_list)
print(type(my_list))
print(my_list[0])

# Unir Sets
my_other_set = {"Arturo", "Mila", "Tony"}
my_new_set = my_set.union(my_other_set)
print(my_new_set)
my_new_new_set = my_set.union({"Mila"})
print(my_new_new_set)
# Tuples - Diferencia con Listas, parentsis por corchetes y los datos no se pueden modificar.

my_tuple = tuple()
my_other_tuple = ()

my_tuple = (37, 1.81, "Guido", "Rimati")
print(my_tuple)
print(type(my_tuple))
print(my_tuple[0])

# Contar
print(my_tuple.count("Guido"))

# Indica Posición
print(my_tuple.index("Guido"))

#Mostrar Seleccion
print(my_tuple[1:3])

# Pasarlo a Lista
my_tuple = list(my_tuple)
print(type(my_tuple))

# Borrarla
del my_tuple
print(my_tuple)
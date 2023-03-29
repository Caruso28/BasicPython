# Lists

my_list = list()
my_other_list = []
print(len(my_list))

my_list = [35, 24, 62, 52, 30, 30, 17]
print(my_list)
print(len(my_list))

# Cuenta
print(my_list.count(62))
print(my_list.count(30))

# Borra
my_list.remove(52)
print(my_list)

my_other_list = [35, 1.77, "Guido", "Rimati"]
print(my_other_list)
print(len(my_other_list))
print(type(my_other_list))

# Ubica
print(my_other_list[1])
print(my_other_list[0])
print(my_other_list[-1])
age, height, name, surname = my_other_list
print(name)

# Agrega al final y agrega donde digas
my_other_list.append("Recalculando")
my_other_list.insert(1, "Programador")
print(my_other_list)

# Concatena
print(my_list + my_other_list)

# Copia
my_new_new_list = my_list.copy()
print(my_new_new_list)

# Ordena
my_list.sort()
print(my_list)
# Dicts

my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {"Nombre":"Guido", "Apellido":"Rimati", "Edad":37} 

my_dict = {
    "Nombre":"Guido", 
    "Apellido":"Rimati", 
    "Edad":37,
    "Hobbies": {"Estudiar", "Deporte"}
    } 

print(my_dict)
print(my_other_dict)

#Buscar algo en particular
print(my_dict["Nombre"])

# Agregar item
my_dict["Calle"] = "Doblas"
print(my_dict)

# Borrar item
del my_dict["Calle"]
print(my_dict)

# Verificar que este en el Dict / Se busca por clave, no por valor
print("Guido" in my_dict)
print("Nombre" in my_dict)

# Motrar todo/clave/valor
print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())

my_new_new_dict = dict.fromkeys(("Nombre"))
print(my_new_new_dict)

my_list = ["Nombre", 1, "Piso"]
my_renew_dict = dict.fromkeys((my_list))
print(my_renew_dict)

# Copiar Dict para aprovechar las claves
my_new_dict = dict.fromkeys((my_dict))
print(my_new_dict)

# Cambiar Dict por List/Set/Tuple
print(list(my_new_dict))
print(tuple(my_new_dict))
print(set(my_new_dict))

print(my_dict.values())
print(list(my_dict.values()))
# Loops

# While

my_condition = 0
while my_condition < 10:
    print (my_condition)
    my_condition += 2

else: # Es opcional
    print("Mi condición es mayor o igual que 10")

# Como romper un loop
while my_condition < 20:
    print(my_condition)
    my_condition += 1
    if my_condition == 15:
        print ("Se detiene la ejecucion")
        break

# For

my_list = [35, 24, 62, 52, 30, 30, 17]
for element in my_list:
    print(element)

my_dict = {
    "Nombre":"Guido", 
    "Apellido":"Rimati", 
    "Edad":37,
    "Hobbies": {"Estudiar", "Deporte"}
    } 
for element in my_dict:
    print(element)
    if element == "Edad":
        break
    print("Se ejecuta")
else:
    print("El bucle for en mi diccionario ha finalizado")
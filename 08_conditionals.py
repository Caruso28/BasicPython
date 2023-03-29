# Conditionals

my_condition = True

if my_condition: # Es lo mismo que deir que my_condition == True
    print("Se ejecuta a condicion del if")

my_condition = 5 * 2

if my_condition == 10:
    print("Es igual que 10")
elif my_condition > 10 and my_condition < 20:
    print("Es mayor que 10 y menor que 20")
elif my_condition >= 20:
    print("Es mayor o igual que 20")
else:
    print("Es menor que 10")


my_string = "Mi cadena de texto"
    
if my_string:
    print("Mi cadena de texto no es vacia")

if my_string == "Mi cadena de texto":
    print("Mi cadena de texto no es vacia")

my_string = ""
if not my_string:
    print("Mi cadena de texto es vacia")

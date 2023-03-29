# Exceptions handling
numberOne = 5 
numberTwo = 1
numberTwo = "1"

# Try Except
try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except:
    print("Se ha producido un error")

# Try Escept Else
try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except:
    print("Se ha producido un error")
else: #Se ejecuta si nose produce un except
    print("La ejecucion continua correctamente")

# Try Except Finally
try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except:
    print("Se ha producido un error")
else: #Se ejecuta si nose produce un except
    print("La ejecucion continua correctamente")
finally: #Se ejecuta siempre
    print("La ejecución continúa")    

# Excepciones por tipo
try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except TypeError:
    print("Se ha producido un TypeError")
except ValueError:
    print("Se ha producido un ValueError")

# Captura de la informacion de la excepcion
try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except ValueError as error: #Identifica que tipo de error es
    print(error)
except Exception as my_exception: # Indicar que el error anterior es una excepcion
    print(my_exception)

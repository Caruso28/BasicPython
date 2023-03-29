 # Modules

# Importar modulos que yo defini
import my_module

my_module.sumValue(5, 3, 1)
my_module.printValue("Hola Python")

from my_module import sumValue, printValue

sumValue = (5, 3, 1)
printValue = ("Hola Python")

# Importar modulos definidos por el sistema
import math

print(math.pi)
print(math.pow(2, 8))

from math import pi as pi_value
print(pi_value)

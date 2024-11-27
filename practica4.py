import random
import matplotlib as plt
import numpy as np


# Estableix la semilla per garantir la repetició de la mateixa seqüència aleatòria
random.seed(42)

# Generar 10 punts aleatoris en el pla (0,0) a (10,10)
punts = [(random.uniform(0, 10), random.uniform(0, 10)) for _ in range(10)]

# Mostrar els punts generats
for punt in punts:
    print(punt)


grid()



import numpy as np
import pandas as pd

# Array de numpy
array_np = np.random.randint(0, 100, size=10)  # Generate an array of 10 random integers between 0 and 100
media = np.mean(array_np)
desviacion = np.std(array_np)
maximo = np.max(array_np)

# DataFrame de pandas
df = pd.DataFrame(array_np, columns=['Valor'])
df['Clasificacion'] = np.where(df['Valor'] >= 50, 'Alto', 'Bajo')  # Assuming 50 as the threshold for classification

print('Media:', media)
print('Desviacion estandar:', desviacion)
print('DataFrame:\n', df.head())
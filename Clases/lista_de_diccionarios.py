import pandas as pd
import numpy as np
import os

df = open('INTRODUCCION POO\Ejercicio-POO-con-archivos\Clases\calificaciones.csv', 'r')
df = pd.read_csv(df, sep = ';')
df = df.sort_values(by = 'Apellidos')
print(df)


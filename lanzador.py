from Clases import *
import pandas as pd

df = open('INTRODUCCION POO\Ejercicio-POO-con-archivos\Clases\calificaciones.csv', 'r')
df = pd.read_csv(df, sep = ';')
print(df)

resultado = Parte_3(df)
print(resultado)

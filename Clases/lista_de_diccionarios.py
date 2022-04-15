import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
df = open('INTRODUCCION POO\Ejercicio-POO-con-archivos\Clases\calificaciones.csv', 'r')
df = pd.read_csv(df, sep = ';')
df = df.sort_values(by = 'Apellidos')

df = df.fillna(0)
columnas = df.columns.values

df['Asistencia'] = df['Asistencia'].str.split('%').apply(lambda x: x.pop(0))
print(df['Asistencia'])
df = df.astype(str)

for i in columnas[2:]:
    df[i] = df[i].str.split(',').apply(lambda x: '.'.join(x[:]))

df[columnas[2:]] = df[columnas[2:]].astype(float)

print(df)
#df.loc[df['Parcial1'] < df['Ordinario1']]

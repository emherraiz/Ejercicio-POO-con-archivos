import pandas as pd
import numpy as np
import os

df = open('INTRODUCCION POO\Ejercicio-POO-con-archivos\Clases\calificaciones.csv', 'r')
DF = pd.DataFrame(df)
print(DF.head())


from Clases.parte_3 import *

import pandas as pd
df = open('INTRODUCCION POO\Ejercicio-POO-con-archivos\Clases\calificaciones.csv', 'r')
df = pd.read_csv(df, sep = ';')
resultado = Parte_3(df)
Resultado = resultado.alumnos_suspensos()


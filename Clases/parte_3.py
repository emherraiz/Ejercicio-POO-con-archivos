from parte_2 import *
import pandas as pd
class Parte_3(Parte_2):
    def __init__(self, df):
        super().__init__(df)

    def alumnos_suspensos(self):
        # Importamos todos los datos ajustados
        df = self.ajustar()
        Aprobado = []
        # Imponemos las condiciones para que un alumno apruebe
        for i in range(len(df)):
            if df.iloc[i, 2] >= 75 and df.iloc[i, 9] >= 4 and df.iloc[i, 10] >= 4 and df.iloc[i, 11] >= 4 and df.iloc[i, 12] >= 5:
                Aprobado.append('Aprobado')
            else:
                Aprobado.append('Suspende')

        df['Aprobado'] = Aprobado

        # Devolvemos el Dataframe final
        return df

    def __str__(self):
        print(df)
        return 'hola3'


df = open('INTRODUCCION POO\Ejercicio-POO-con-archivos\Clases\calificaciones.csv', 'r')
df = pd.read_csv(df, sep = ';')

Resultado = Parte_3

print(Resultado(df))

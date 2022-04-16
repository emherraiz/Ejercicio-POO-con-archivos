from parte_1 import Parte_1
import pandas as pd
class Parte_2(Parte_1):
    def __init__(self, df):
        super().__init__(df)

    def ajustar(self):
        # Primero ordenamos por apellidos
        df = self.ordenar()

        # Rellenamos con 0 las celdas vacías
        df = df.fillna(0)
        columnas = df.columns.values

        # Quitamos el porcentaje para poder pasarlo a float
        df['Asistencia'] = df['Asistencia'].str.split('%').apply(lambda x: x.pop(0))

        # Lo pasamos todo a string para luego devolver como float
        df = df.astype(str)

        # Cambiamos las comas por puntos, ya que astype() no entiende las comas como un decimal
        for i in columnas[2:]:
            df[i] = df[i].str.split(',').apply(lambda x: '.'.join(x[:]))

        # Ahora, a partir de la segunda columna (apellidos) cambiamos a float para poder operar
        df[columnas[2:]] = df[columnas[2:]].astype(float)

        # Creamos listas vacias donde añadiremos las notas finales
        nota_final_parcial_1 = list()
        nota_final_parcial_2 = list()
        nota_final_practicas = list()

        # Cada i es una fila(alumno), del cual nos quedaremos con su mejor nota de cada convocatoria
        for i in range(len(df)):
            if df.iloc[i, 3] > df.iloc[i, 5]:
                nota_final_parcial_1_i = df.iloc[i, 3]
            else:
                nota_final_parcial_1_i = df.iloc[i, 5]
            nota_final_parcial_1.append(nota_final_parcial_1_i)


            if df.iloc[i, 4] > df.iloc[i, 6]:
                nota_final_parcial_2_i = df.iloc[i, 4]
            else:
                nota_final_parcial_2_i = df.iloc[i, 6]
            nota_final_parcial_2.append(nota_final_parcial_2_i)


            if df.iloc[i, 7] > df.iloc[i, 8]:
                nota_final_practica_i = df.iloc[i, 7]
            else:
                nota_final_practica_i = df.iloc[i, 8]
            nota_final_practicas.append(nota_final_practica_i)

        # Creamos nuestras nuevas columnas en el DataFrame
        df['Nota Parcial 1'] = nota_final_parcial_1
        df['Nota Parcial 2'] = nota_final_parcial_2
        df['Nota Practicas'] = nota_final_practicas

        # Esta ultima es la nota final
        df['Nota final'] = (df['Nota Parcial 1'] + df['Nota Parcial 2']) * .3 + df['Nota Practicas'] * .4

        return df

    def __str__(self):
        print(df)
        return 'hola'



df = open('INTRODUCCION POO\Ejercicio-POO-con-archivos\Clases\calificaciones.csv', 'r')
df = pd.read_csv(df, sep = ';')


Resultado = Parte_2(df)

print(Resultado.ajustar())

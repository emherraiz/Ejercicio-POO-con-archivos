# Ejercicio-POO-con-archivos
## Link del repositorio
https://github.com/emherraiz/Ejercicio-POO-con-archivos

## Enunciado

El fichero calificaciones.csv contiene las calificaciones de un curso. Durante el curso se realizaron dos exámenes parciales de teoría y un examen de prácticas. Los alumnos que tuvieron menos de 4 en alguno de estos exámenes pudieron repetirlo en la al final del curso (convocatoria ordinaria). Escribir un programa que contenga las siguientes funciones:

1 - Una función que reciba el fichero de calificaciones y devuelva una lista de diccionarios, donde cada diccionario contiene la información de los exámenes y la asistencia de un alumno. La lista tiene que estar ordenada por apellidos.

2 - Una función que reciba una lista de diccionarios como la que devuelve la función anterior y añada a cada diccionario un nuevo par con la nota final del curso. El peso de cada parcial de teoría en la nota final es de un 30% mientras que el peso del examen de prácticas es de un 40%.

3 - Una función que reciba una lista de diccionarios como la que devuelve la función anterior y devuelva dos listas, una con los alumnos aprobados y otra con los alumnos suspensos. Para aprobar el curso, la asistencia tiene que ser mayor o igual que el 75%, la nota de los exámenes parciales y de prácticas mayor o igual que 4 y la nota final mayor o igual que 5.


## Solucion

### Parte 1:

class Parte_1:
    def __init__(self, df):
        self.df = df

    def ordenar(self):
        ordenado = self.df.sort_values(by = 'Apellidos')
        return ordenado

### Parte 2:

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

### Parte 3:

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

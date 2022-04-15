import pandas as pd
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

nota_final = list()
nota_final_parcial_1 = list()
nota_final_parcial_2 = list()
nota_final_practicas = list()
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

df['Nota Parcial 1'] = nota_final_parcial_1
df['Nota Parcial 2'] = nota_final_parcial_2
df['Nota Practicas'] = nota_final_practicas
df['Nota final'] = (df['Nota Parcial 1'] + df['Nota Parcial 2']) * .3 + df['Nota Practicas'] * .4

print(df['Asistencia'][6])

Aprobado = []
for i in range(len(df)):
    if df.iloc[i, 2] >= 75 and df.iloc[i, 9] >= 4 and df.iloc[i, 10] >= 4 and df.iloc[i, 11] >= 4 and df.iloc[i, 12] >= 5:
        Aprobado.append('Aprobado')
    else:
        Aprobado.append('Suspende')

df['Aprobado'] = Aprobado

print(df)



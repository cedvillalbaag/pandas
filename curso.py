import pandas as pd
import numpy as np


pd.set_option('display.max_columns', 20)

#Extraer data de csv
df_excel = pd.read_csv('StudentsPerformance.csv')

df_excel.describe()

df_excel.sum()

#Contar filas por columnas
df_excel.count()


# promedio
df_excel['average'] = np.mean(df_excel, axis = 1)

# Funcion SI
df_excel['pass/fail'] =  np.where(df_excel['average'] > 70, 'pass', 'fail')


#Funcion SI con varias condicionales
conditions = [ 
			(df_excel['average'] >= 90),
			(df_excel['average'] >= 80) & (df_excel['average'] < 90),
			(df_excel['average'] >= 70) & (df_excel['average'] < 80),
			(df_excel['average'] >= 60) & (df_excel['average'] < 70),
			(df_excel['average'] < 60)	
]

# Crear lista de valores para cada condicion definida
values = ['A','B','C','D','E']

df_excel['grades'] = np.select(conditions, values)


# Funcion Contar SI
#print(df_excel[df_excel['gender'] == 'female'].count())


# Funcion Sumar con varios criterios
#Obtener el promedio para genero femenimo y grupo B

#primero aplicar los filtros
df_2 = df_excel[(df_excel['gender'] == 'female') & (df_excel['race/ethnicity'] == 'group B')]
# segundo, utilizar el metodo deseado
print(df_2.sum(axis = 1))



 



import streamlit as st

# Configuración de la página
st.set_page_config(   
    page_icon="📌",
    layout="wide"
)

st.title("Momento 2 - Actividad 5")

st.header("Descripción de la actividad")
st.markdown("""
Esta actividad es una introducción práctica a Python y a las estructuras de datos básicas.
En ella, exploraremos los conceptos fundamentales de Python y aprenderemos a utilizar variables,
tipos de datos, operadores, y las estructuras de datos más utilizadas como listas, tuplas,
diccionarios y conjuntos.
""")

st.header("Objetivos de aprendizaje")

st.markdown("""
- Comprender los tipos de datos básicos en Python
- Aprender a utilizar variables y operadores
- Dominar las estructuras de datos fundamentales
- Aplicar estos conocimientos en ejemplos prácticos
""")

st.header("Solución")
import streamlit as st
import pandas as pd

# Título de la aplicación
st.title("📊 Actividad 5 - Agregar, Agrupar y Fusionar Datos en Pandas")

# Crear un DataFrame inicial con algunos datos de ejemplo
df1 = pd.DataFrame({
    'ID': [1, 2, 3, 4],
    'Nombre': ['Ana', 'Luis', 'Marta', 'Pedro'],
    'Curso': ['Matemáticas', 'Historia', 'Física', 'Química']
})

df2 = pd.DataFrame({
    'ID': [1, 2, 5],
    'Nota': [8.5, 7.0, 9.0]
})

# Mostrar el DataFrame inicial
st.subheader("📋 Datos Iniciales")
st.write("Primer DataFrame de Estudiantes:")
st.dataframe(df1)

st.write("Segundo DataFrame de Notas:")
st.dataframe(df2)

# Sección 1: Agregar filas y columnas
st.sidebar.header("🔄 Agregar Datos")

# Agregar filas
st.sidebar.subheader("Agregar nueva fila")
nuevo_id = st.sidebar.number_input("ID", min_value=1, max_value=999, step=1)
nuevo_nombre = st.sidebar.text_input("Nombre")
nuevo_curso = st.sidebar.selectbox("Curso", ['Matemáticas', 'Historia', 'Física', 'Química'])
nueva_nota = st.sidebar.number_input("Nota", min_value=0.0, max_value=10.0, step=0.1)

if st.sidebar.button("Agregar fila"):
    nueva_fila = pd.DataFrame({
        'ID': [nuevo_id],
        'Nombre': [nuevo_nombre],
        'Curso': [nuevo_curso]
    })
    df1 = pd.concat([df1, nueva_fila], ignore_index=True)
    st.write("Fila agregada correctamente")
    st.dataframe(df1)

# Agregar columna
st.sidebar.subheader("Agregar nueva columna")
nombre_columna = st.sidebar.text_input("Nombre de la columna nueva")
valor_columna = st.sidebar.number_input("Valor para la nueva columna", min_value=0, max_value=100, step=1)

if st.sidebar.button("Agregar columna"):
    df1[nombre_columna] = valor_columna
    st.write(f"Columna '{nombre_columna}' agregada correctamente.")
    st.dataframe(df1)

# Sección 2: Agrupar datos
st.sidebar.header("📊 Agrupar Datos")

# Agrupar por "Curso" y realizar una operación de conteo
grupo_curso = df1.groupby('Curso').size()
st.write("Conteo de estudiantes por curso:")
st.dataframe(grupo_curso)

# Agrupar por "Curso" y calcular el promedio de "Nota" (considerando que tenemos que fusionar con df2)
df_combinado = pd.merge(df1, df2, on="ID", how="left")
grupo_promedio = df_combinado.groupby('Curso')['Nota'].mean()
st.write("Promedio de notas por curso:")
st.dataframe(grupo_promedio)

# Sección 3: Fusionar datos
st.sidebar.header("🔗 Fusionar Datos")

# Seleccionar tipo de fusión
tipo_fusion = st.sidebar.selectbox("Selecciona el tipo de fusión", ["inner", "left", "right", "outer"])

# Fusionar los DataFrames df1 y df2
fusion = pd.merge(df1, df2, on="ID", how=tipo_fusion)
st.write(f"Fusión tipo '{tipo_fusion}':")
st.dataframe(fusion)

# Resumen final
st.subheader("🔍 Resumen Final")
st.write("DataFrame combinado y modificado después de todas las operaciones:")
st.dataframe(df1)



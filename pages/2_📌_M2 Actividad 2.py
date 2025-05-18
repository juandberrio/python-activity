import streamlit as st

# Configuración de la página
st.set_page_config(   
    page_icon="📌",
    layout="wide"
)

st.title("Momento 2 - Actividad 2")

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
import io  

# Título de la aplicación
st.title("📊 Análisis de Estudiantes en Colombia")

# Cargar los datos
try:
    df = pd.read_csv("estudiantes_colombia.csv")
except FileNotFoundError:
    st.error("❌ No se encontró el archivo 'estudiantes_colombia.csv'. Asegúrate de que esté en el mismo directorio que este script.")
    st.stop()

# Mostrar las primeras y últimas 5 filas
st.subheader("📌 Primeras 5 filas del dataset")
st.dataframe(df.head())

st.subheader("📌 Últimas 5 filas del dataset")
st.dataframe(df.tail())

# Mostrar resumen con .info()
st.subheader("📄 Información general del dataset")
buffer = io.StringIO()
df.info(buf=buffer)
st.text(buffer.getvalue())

# Mostrar .describe()
st.subheader("📊 Estadísticas descriptivas")
st.dataframe(df.describe())

# Selección de columnas específicas
st.subheader("📌 Selección de columnas")
columnas = st.multiselect("Selecciona las columnas que deseas visualizar", df.columns.tolist(), default=["nombre", "edad", "promedio"])
st.dataframe(df[columnas])

# Filtro por promedio usando un slider
st.subheader("🎯 Filtrar estudiantes por promedio")
promedio_minimo = st.slider("Selecciona el promedio mínimo", min_value=0.0, max_value=5.0, step=0.1, value=4.0)
filtro_promedio = df[df["promedio"] >= promedio_minimo]
st.write(f"Estudiantes con promedio mayor o igual a {promedio_minimo}:")
st.dataframe(filtro_promedio)

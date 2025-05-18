import streamlit as st
import pandas as pd


# Configuración de la página
st.set_page_config(   
    page_icon="📌",
    layout="wide"
)

st.title("Momento 2 - Actividad 1")

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
import numpy as np
import sqlite3
import os
import json


st.title("Actividad 1 - Creación de DataFrames")
st.markdown("Esta actividad tiene como objetivo practicar la creación de distintos tipos de DataFrames con Pandas y posteriormente reflejarlo en Streamlit.")


st.subheader("📚 DataFrame de Libros (desde diccionario)")
libros = {
    "título": ["bueno bonito y carito", "Cien años de soledad", "Los vagabundos de Dios", "la Pobre Viejecita"],
    "autor": ["David Gomez","Gabriel García Márquez", "Mario Mendoza","Rafael Pombo"],
    "año de publicación": [2017, 1967,2024,1854],
    "género": ["Ventas", "Realismo mágico", "Novela", "Poema"]
}
df_libros = pd.DataFrame(libros)
st.dataframe(df_libros)


st.subheader("🏙️ Información de Ciudades (desde lista de diccionarios)")
ciudades = [
    {"nombre": "Bogotá", "población": 8000000, "país": "Colombia"},
    {"nombre": "Lima", "población": 9500000, "país": "Perú"},
    {"nombre": "Buenos Aires", "población": 3000000, "país": "Argentina"},
]
df_ciudades = pd.DataFrame(ciudades)
st.dataframe(df_ciudades)


st.subheader("🛒 Productos en Inventario (desde lista de listas)")
productos = [
    ["Llantas", 150, 25],
    ["Rines", 80, 40],
    ["Farolas", 800, 10]
]
df_productos = pd.DataFrame(productos, columns=["Producto", "Precio", "Stock"])
st.dataframe(df_productos)


st.subheader("👥 Datos de Personas (desde Series)")
nombres = pd.Series(["Alberto", "Luis", "Cristian", "Manuela"])
edades = pd.Series([28, 34, 20, 36])
ciudades = pd.Series(["Bogotá", "Medellin", "Barranquilla", "Cali"])
df_personas = pd.DataFrame({"Nombre": nombres, "Edad": edades, "Ciudad": ciudades})
st.dataframe(df_personas)

import pandas as pd
import os
import json

# Función para mostrar errores si ocurre algún problema
def cargar_archivo_safely(funcion_lectura, ruta, nombre):
    try:
        df = funcion_lectura(ruta)
        st.dataframe(df)
    except Exception as e:
        st.error(f"❌ Error al cargar {nombre}: {e}")

# 1. CSV
csv_path = "data.csv"
if not os.path.exists(csv_path):
    df_csv = pd.DataFrame({
        "id": [1, 2, 3],
        "nombre": ["Producto A", "Producto B", "Producto C"],
        "valor": [100, 150, 200]
    })
    df_csv.to_csv(csv_path, index=False)
    st.success("✅ Archivo data.csv fue creado.")

st.subheader("Validación: Datos desde CSV")
cargar_archivo_safely(pd.read_csv, csv_path, "data.csv")

# 2. Excel
excel_path = "data.xlsx"
if not os.path.exists(excel_path):
    df_excel = pd.DataFrame({
        "producto": ["Lápiz", "Cuaderno", "Mochila"],
        "precio": [0.50, 1.50, 15.00],
        "stock": [100, 200, 50]
    })
    df_excel.to_excel(excel_path, index=False)
    st.success("✅ Archivo data.xlsx fue creado.")

st.subheader("Validación: Datos desde Excel")
cargar_archivo_safely(pd.read_excel, excel_path, "data.xlsx")

# 3. JSON
json_path = "data.json"
if not os.path.exists(json_path):
    usuarios = [
        {"nombre": "Juan", "correo": "juan@email.com"},
        {"nombre": "Ana", "correo": "ana@email.com"},
        {"nombre": "Luis", "correo": "luis@email.com"}
    ]
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(usuarios, f, ensure_ascii=False, indent=4)
    st.success("✅ Archivo data.json fue creado.")

st.subheader("Validación: Datos de Usuarios desde JSON")
cargar_archivo_safely(pd.read_json, json_path, "data.json")

# 8. Desde URL
st.subheader("Datos desde URL")
url = "https://people.sc.fsu.edu/~jburkardt/data/csv/hw_200.csv"
df_url = pd.read_csv(url)
st.dataframe(df_url)

# 9. SQLite
st.subheader("Datos desde SQLite")
conexion = sqlite3.connect("estudiantes.db")
cursor = conexion.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS calificaciones (nombre TEXT, calificación INTEGER)")
cursor.execute("DELETE FROM calificaciones")
cursor.executemany("INSERT INTO calificaciones VALUES (?, ?)", [
    ("Pedro", 85), ("Lucía", 90), ("Marcos", 78)
])
conexion.commit()
df_sqlite = pd.read_sql("SELECT * FROM calificaciones", conexion)
st.dataframe(df_sqlite)
conexion.close()

# 10. NumPy
st.subheader("Datos desde NumPy")
array = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
df_numpy = pd.DataFrame(array, columns=["Columna A", "Columna B", "Columna C"])
st.dataframe(df_numpy)




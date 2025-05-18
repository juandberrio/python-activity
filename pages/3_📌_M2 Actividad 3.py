import streamlit as st

# Configuración de la página
st.set_page_config(   
    page_icon="📌",
    layout="wide"
)

st.title("Momento 2 - Actividad 3")

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
from datetime import datetime  

# Título de la aplicación
st.title("🔍 Filtros Dinámicos - Trabajadores de Colombia")

# Cargar el DataFrame
try:
    df = pd.read_csv("trabajadores_colombia.csv", parse_dates=["fecha_nacimiento"])
except FileNotFoundError:
    st.error("❌ Archivo no encontrado: 'trabajadores_colombia.csv'. Verifica que esté en el mismo directorio.")
    st.stop()

df_filtrado = df.copy()
st.sidebar.header("🎛️ Filtros")

# 1. Filtro por rango de edad
if st.sidebar.checkbox("Filtrar por rango de edad"):
    edad_min, edad_max = st.sidebar.slider("Selecciona el rango de edad", 15, 75, (18, 30))
    df_filtrado = df_filtrado[df_filtrado['edad'].between(edad_min, edad_max)]

# 2. Filtro por municipios
municipios = ['Barranquilla', 'Santa Marta', 'Cartagena', 'Bogotá', 'Medellín',
              'Tunja', 'Manizales', 'Cali', 'Quibdó', 'Buenaventura',
              'Villavicencio', 'Yopal', 'Leticia', 'Puerto Inírida']
if st.sidebar.checkbox("Filtrar por municipios"):
    seleccionados = st.sidebar.multiselect("Selecciona municipios", municipios)
    if seleccionados:
        df_filtrado = df_filtrado[df_filtrado['municipio'].isin(seleccionados)]

# 3. Filtro por ingreso mensual mínimo
if st.sidebar.checkbox("Filtrar por ingreso mensual mínimo"):
    ingreso_min = st.sidebar.slider("Ingreso mensual mínimo", 800_000, 12_000_000, 1_000_000, step=100_000)
    df_filtrado = df_filtrado[df_filtrado['ingreso_mensual'] > ingreso_min]

# 4. Filtro por ocupación
ocupaciones = ['Estudiante', 'Docente', 'Comerciante', 'Agricultor', 'Ingeniero',
               'Médico', 'Desempleado', 'Pensionado', 'Emprendedor', 'Obrero']
if st.sidebar.checkbox("Filtrar por ocupación"):
    seleccionadas = st.sidebar.multiselect("Selecciona ocupaciones", ocupaciones)
    if seleccionadas:
        df_filtrado = df_filtrado[df_filtrado['ocupacion'].isin(seleccionadas)]

# 5. Filtro por tipo de vivienda no propia
if st.sidebar.checkbox("Filtrar personas sin vivienda propia"):
    df_filtrado = df_filtrado[~(df_filtrado['tipo_vivienda'] == 'Propia')]

# 6. Filtro por nombre contiene texto
if st.sidebar.checkbox("Filtrar por nombre"):
    texto = st.sidebar.text_input("Ingresa texto para buscar en nombres", "")
    if texto:
        df_filtrado = df_filtrado[df_filtrado['nombre_completo'].str.contains(texto, case=False, na=False)]

# 7. Filtro por año de nacimiento
if st.sidebar.checkbox("Filtrar por año de nacimiento"):
    años = list(range(1949, 2010))
    año_seleccionado = st.sidebar.selectbox("Selecciona el año", años)
    df_filtrado = df_filtrado[df_filtrado['fecha_nacimiento'].dt.year == año_seleccionado]

# 8. Filtro por acceso a internet
if st.sidebar.checkbox("Filtrar por acceso a internet"):
    acceso = st.sidebar.radio("¿Tiene acceso a internet?", ["Sí", "No"])
    df_filtrado = df_filtrado[df_filtrado['acceso_internet'] == (acceso == "Sí")]

# 9. Filtro por ingresos nulos
if st.sidebar.checkbox("Filtrar por ingresos nulos"):
    df_filtrado = df_filtrado[df_filtrado['ingreso_mensual'].isnull()]

# 10. Filtro por rango de fechas de nacimiento
if st.sidebar.checkbox("Filtrar por rango de fechas de nacimiento"):
    fecha_inicio = st.sidebar.date_input("Fecha de inicio", datetime(1950, 1, 1))
    fecha_fin = st.sidebar.date_input("Fecha de fin", datetime(2000, 12, 31))
    df_filtrado = df_filtrado[df_filtrado['fecha_nacimiento'].between(pd.to_datetime(fecha_inicio), pd.to_datetime(fecha_fin))]

# Mostrar resultados
st.subheader("📋 Datos filtrados")
st.write(f"Total registros: {df_filtrado.shape[0]}")
st.dataframe(df_filtrado)


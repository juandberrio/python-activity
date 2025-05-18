import streamlit as st

# Configuración de la página
st.set_page_config(   
    page_icon="📌",
    layout="wide"
)

st.title("Momento 2 - Actividad 4")

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
st.title("💼 Aplicación Interactiva de Empleados")

# Cargar datos (simulando con un DataFrame simple)
data = {
    'ID': [1, 2, 3, 4, 5],
    'Nombre': ['Juan', 'Ana', 'Carlos', 'Maria', 'Pedro'],
    'Edad': [28, 34, 29, 41, 30],
    'Salario': [3000, 3500, 4000, 4500, 3200],
    'Departamento': ['Ventas', 'Marketing', 'IT', 'HR', 'IT']
}

df = pd.DataFrame(data)

# Mostrar el DataFrame inicial
st.subheader("📋 Datos Iniciales de Empleados")
st.dataframe(df)

# Sección 1: Selección de filas usando .iloc
st.sidebar.header("🚀 Selección usando .iloc")
row_index = st.sidebar.slider("Selecciona una fila para visualizar con .iloc", 0, len(df)-1, 0)
st.write(f"Fila seleccionada con .iloc para índice {row_index}:")
st.write(df.iloc[row_index])

# Sección 2: Selección de filas usando .loc (por nombre)
st.sidebar.header("🧐 Selección usando .loc")
nombre_empleado = st.sidebar.selectbox("Selecciona un empleado por su nombre", df['Nombre'])
empleado = df.loc[df['Nombre'] == nombre_empleado]
st.write(f"Empleado seleccionado con .loc: {empleado}")

# Sección 3: Modificar valores con .loc
st.sidebar.header("✍️ Modificar datos con .loc")
modificar = st.sidebar.checkbox("Modificar salario de un empleado")
if modificar:
    nombre_modificar = st.sidebar.selectbox("Selecciona un empleado para modificar su salario", df['Nombre'])
    nuevo_salario = st.sidebar.number_input(f"Ingrese el nuevo salario de {nombre_modificar}", min_value=0, value=3500, step=100)
    df.loc[df['Nombre'] == nombre_modificar, 'Salario'] = nuevo_salario
    st.write(f"Salario de {nombre_modificar} actualizado a {nuevo_salario}")
    st.dataframe(df)

# Sección 4: Filtro por condición usando .loc
st.sidebar.header("🔍 Filtrar datos con .loc")
filtro_edad = st.sidebar.slider("Selecciona un rango de edad para filtrar empleados", 20, 60, (25, 40))
empleados_filtrados = df.loc[df['Edad'].between(filtro_edad[0], filtro_edad[1])]
st.write(f"Empleados con edad entre {filtro_edad[0]} y {filtro_edad[1]}:")
st.dataframe(empleados_filtrados)

# Sección 5: Selección de varias filas usando .iloc
st.sidebar.header("🔄 Selección múltiple usando .iloc")
filas_seleccionadas = st.sidebar.multiselect("Selecciona múltiples índices de filas para ver con .iloc", list(df.index), default=[0])
df_seleccionado_iloc = df.iloc[filas_seleccionadas]
st.write(f"Filas seleccionadas con .iloc:")
st.dataframe(df_seleccionado_iloc)

# Resumen de cambios
st.subheader("📊 Resumen Final del DataFrame")
st.write(f"Total empleados después de cambios: {df.shape[0]}")
st.dataframe(df)



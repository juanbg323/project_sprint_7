import pandas as pd
import plotly.graph_objects as go  # Importación de plotly.graph_objects como go
import streamlit as st

# Leer los datos del archivo CSV
car_data = pd.read_csv(r'E:\Educacion\Data science\TripleTen\sprint_7\project_7\project_sprint_7\vehicles_us.csv')


st.header("Análisis Exploratorio de Datos de Vehículos en EE.UU.")

build_histogram = st.checkbox("Mostrar Histograma de distribucion de odometros")
build_scatter = st.checkbox("Mostrar Scatter plot de odometro vs precio")

if build_histogram:
    
    st.write("### Histograma de Distribución de Odómetros")# Título del histograma

    # Crear un histograma utilizando plotly.graph_objects
    fig = go.Figure(data=[go.Histogram(x=car_data['odometer'])])

    # Opcional: Puedes añadir un título al gráfico si lo deseas
    fig.update_layout(title_text='Distribución de Odómetros')

    # Mostrar el gráfico Plotly en Streamlit
    st.plotly_chart(fig, use_container_width=True)

elif build_scatter:
    
    st.write("### Scatter Plot de Odómetro vs Precio")# Título del scatter plot

    # Crear un scatter plot utilizando plotly.graph_objects
    fig = go.Figure(data=[go.Scatter(x=car_data['odometer'], y=car_data['price'], mode='markers')])

    # Opcional: Puedes añadir un título al gráfico si lo deseas
    fig.update_layout(title_text='Relación entre Odómetro y Precio')

    # Mostrar el gráfico Plotly en Streamlit
    st.plotly_chart(fig, use_container_width=True)

       
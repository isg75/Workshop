import streamlit as st 
from PIL import Image 

import matplotlib.pyplot as plt 
import matplotlib

import seaborn as sns
import pandas as pd 
import numpy as np

import folium
from streamlit_folium import st_folium

data = '../data/squirrelsNYC.csv'


st.markdown('# Introduction al análisis de datos')
st.markdown('### Ardillas en Central Park, NYC')


if st.button("Meet the Squirrels"):
    img=Image.open('../images/ardilla_gris.jpeg')
    st.image(img,width=400, caption="Ardilla gris")
    img=Image.open('../images/ardilla_negra.jpeg')
    st.image(img,width=400, caption="Ardilla negra")
    img=Image.open('../images/ardilla_cinamon.jpeg')
    st.image(img,width=400, caption="Ardilla canela")
st.markdown(
   "Los datos fueron obtenidos de **[NYC open source data](https://data.cityofnewyork.us/Environment/2018-Central-Park-Squirrel-Census-Squirrel-Data/vfnx-vebw)**.")



st.sidebar.markdown("## Side Panel")
st.sidebar.markdown('### Usa este panel para explorar el dataset y obtener distintas visualizaciones')
df = pd.read_csv(data)
lowercase = lambda x:str(x).lower()
df.rename(lowercase, axis='columns',inplace=True)

st.header('Listo para explorar las ardillas de central Park, NYC')

# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Leyendo squirrelsNYC dataset...')

    # Notify the reader that the data was successfully loaded.
data_load_state.text('Cargando los datos...Completado')
images=Image.open('../images/ardilla_excitada.jpeg')
st.title('¡Hurra!')
st.image(images,width=100)


# Showing the original raw data
if st.checkbox("Mostrar datos originales", False):
    st.subheader('Datos originales')
    st.write(df)
st.title('Exploración rápida')
st.sidebar.subheader(' Exploración rápida')
st.markdown("Marca la casila del panel lateral para explorar el dataset")
if st.sidebar.checkbox('Información básica'):
    if st.sidebar.checkbox('Análisis preliminar'):
        st.subheader('Análisis preliminar:')
        st.write(df.head())
    if st.sidebar.checkbox("Mostrar columnas"):
        st.subheader('Mostrar lista de columnas')
        all_columns = df.columns.to_list()
        st.write(all_columns)
   
    if st.sidebar.checkbox('Resumen estadístico'):
        st.subheader('Resumen estadístico')
        st.write(df.describe())
    if st.sidebar.checkbox('Valores nulos'):
        st.subheader('Valores nulos')
        st.write(df.isnull().sum())

st.set_option('deprecation.showPyplotGlobalUse', False)

st.title('Gráficos')
st.markdown("Selecciona el tipo de gráfico deseado")
st.sidebar.subheader('Selección de gráfico')
if st.sidebar.checkbox('Gráfico'):

    if st.sidebar.checkbox('Mapa de avistamientos'): 
        st.subheader('Avistamientos')  
        m = folium.Map(location=[40.781781, -73.966787], zoom_start=14)

        for i in range(len(df)):
            folium.CircleMarker(
            location=[df.iloc[i,1],df.iloc[i,0]],
            radius=2,
            icon=folium.Icon(icon="cloud")).add_to(m)
    
        st_data = st_folium(m, width=725)

    if st.sidebar.checkbox('Gráfico de frecuencia'):
        st.subheader('Gráfico de frecuencia')
        st.info("En caso de error, por favor selecciona una columna adecuada en el panel lateral")
        column_count_plot = st.sidebar.selectbox("Escoge la columna a explorar. Prueba seleccionando 'age",df.columns)
        hue_opt = st.sidebar.selectbox("Variable categórica opcional (hue). Prueba seleccionando 'primary_fur_color' ",df.columns.insert(0,None))
        
        fig = sns.countplot(x=column_count_plot,data=df,hue=hue_opt)
        st.pyplot()

    if st.sidebar.checkbox('Histograma | Distribución'):
        st.subheader('Histograma | Distribución')
        st.info("En caso de error, por favor selecciona una columna adecuada en el panel lateral")
        # if st.checkbox('Dist plot'):
        column_dist_plot = st.sidebar.selectbox("Variable categórica opcional (hue). Prueba seleccionando 'tail_twitches'",df.columns)
        fig = sns.distplot(df[column_dist_plot])
        st.pyplot()
                        
        
    if st.sidebar.checkbox('Boxplot'):
        st.subheader('Boxplot')
        st.info("En caso de error, selecciona una columna adecuada en el panel lateral")
        column_box_plot_X = st.sidebar.selectbox("X (Escoge una columna). Prueba seleccionando 'shift':",df.columns.insert(0,None))
        column_box_plot_Y = st.sidebar.selectbox("Y (Escoge una columna numérica). Prueba seleccionando 'Any Activity'",df.columns)
        hue_box_opt = st.sidebar.selectbox("Variable categórica opcional (boxplot hue)",df.columns.insert(0,None))
        # if st.checkbox('Plot Boxplot'):
        fig = sns.boxplot(x=column_box_plot_X, y=column_box_plot_Y,data=df,palette="Set3")
        st.pyplot()




st.sidebar.info("[Data Source](https://data.cityofnewyork.us/Environment/2018-Central-Park-Squirrel-Census-Squirrel-Data/vfnx-vebw)")
st.sidebar.info(" [Source Article](https://towardsdatascience.com/build-your-first-data-visualization-web-app-in-python-using-streamlit-37e4c83a85db)")
st.sidebar.info("Self Exploratory Visualization on palmerpenguins Code - Brought To you By [Mala Deep](https://github.com/maladeep)  ")
st.sidebar.text("Built with  ❤️ Streamlit")











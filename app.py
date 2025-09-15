import streamlit as st
import pandas as pd
import plotly_express as px

car_data = pd.read_csv("vehicles_us.csv")

st.header('Construir un histograma para el conjunto de datos de anuncio de venat de coches')
hist_checkbox = st.checkbox('Construir histograma') # craer una casilla de verificacion

if hist_checkbox: #al hacer click en el boton
    #escribir mensaje
    st.write('Creacion de un histograma para el conjunto de datos de anuncios de ventas de coche')
    
    #crear un histograma
    fig = px.histogram(car_data, x = 'odometer')

    #mostrar grafico plotly interactivo
    st.plotly_chart(fig, use_container_width=True)



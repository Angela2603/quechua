## leer excel
import pandas as pd

verbos = pd.read_excel('verbos.xlsx')

## diccionario

quechua = list(verbos['quechua'])
espanol = list(verbos['espanol'])

dict_que_esp = dict(zip(quechua,espanol))

## importamos streamlit
import streamlit as st

option = st.selectbox(
    "Seleccione un verbo en quechua",
    (quechua))
st.write("El verbo en español es", dict_que_esp[option])

persona = st.radio(
    'Selecciona la persona',
    ['Primera','Segunda','Tercera','Cuarta'])

numero = st.radio(
    'Selecciona el número',
    ['Singular','Plural'])

tiempo = st.selectbox(
    'Selecciona el tiempo',
    ['Presente','Pasado'])

if tiempo == 'Presente':
    aspecto = st.radio(
        'Seleeciona el aspecto',
        ['Simple','Progresivo','Habitual'])

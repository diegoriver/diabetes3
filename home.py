import streamlit as st
from functions import *

st.set_page_config(
    page_title="Inicio",
    page_icon="👋",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)

html_temp = """
    <h1 style="color:#181082;text-align:center;">SISTEMA DE PREDICCIÓN DE DIABETES CON UNA RED NEURONAL PROFUNDA</h1>
    """
st.markdown(html_temp, unsafe_allow_html=True)


st.markdown(
    """
    Este sistema desarrollado ha sido estructurado en dos modos y tres pasos.
    #

    ### MODOS

    Este sistema para predicción de diabetes se puede desarrollar de dos modos:
      
      - Modo individual: se llena un formulario por cada paciente.
      
      - Modo por lotes: procesando un lote de pacientes (para esto se provee un archivo excel con información de ejemplo de pacientes).
    
    Las anteriores opciones las puede escoger el usuario en el menu de la izquierda.

    ##
    ### PASOS DEL PROCESO


    - PASO 0: Ene ste paso se hace la creación de los inputs, estos son archivos .json de la carpeta 
    inputs con la información propia de cada paciente cumpliendo los parámetros con los cuales se 
    entrenó el modelo de calsificación.

        Es de mencionar que en un modelo en producción se asume que los inputs provienen de un proceso
      anterior, el cual lo simulamos en este paso, tanto en el modo individual o el modo por lotes
      se crean los inputs

    
    - PASO 1: En este paso se obtiene los resultados de la predicción utilizando el modelo de 
    entrenado y se procede a crear los archivos de salida .json en la carpeta outputs con los 
    resultados obtenidos.


    - PASO 2: En este paso se cargan los resultados de la carpeta outputs y se procede a la 
    visualización de los mismos.
    """
)
 

html = """
<div style="color: lightgray;">
    Created by <a href="https://www.linkedin.com/in/diego-rivera-ai/" 
    style="color: lightgray; !important; text-decoration: none !important;">Diego Rivera</a>
</div>
"""
st.markdown(html, unsafe_allow_html=True)

    
    

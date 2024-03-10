import streamlit as st
import pandas as pd
from functions import *
import os


def prediction_lote():  
    # Título
    html_temp = """
    <h1 style="color:#181082;text-align:center;">Test de diabetes por lotes de pacientes</h1>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    if st.button("PASO 0: creación de inputs"):
        
        st.markdown(
        """
        Para facilidad se va a cargar el archivo excel datos_pacientes.xlsx previamente construido 
        con datos de pacientes que se va a utilizar para la creación de los inputs,
        con el fin de realizar una prueba del funcionamiento del sistema por lotes.
        """
        )
        
        
        numero_inputs = create_inputs_lote_pacientes()
        st.markdown(f"Se han creando {numero_inputs} inputs de pacientes")


    if st.button("PASO 1 y PASO 2"):
        
        st.markdown("##### PASO 1: predicción y creacion de outputs")

        st.markdown(
        """
        Se procede a procesar los inputs generados en el paso anterior y crear los outputs con 
        los resultados obtenidos de las predicciones.
        """
        )

        ruta_inputs = "inputs"

        results = []

        for nombre_archivo in os.listdir(ruta_inputs): # Lee los nombres de los inputs en la carpeta
            if nombre_archivo.endswith(".json"):
                                
                # quita la extension .json
                id_num = os.path.splitext(nombre_archivo)[0]                 
                # hace la prediccion de cada input
                _ , nodiabetico, prediabetico, diabetico = prediction_individual(id_num)

                # carga los valores medicos de ese input
                x_in = load_input(id_num)                
                # crea los resultados de salida
                create_output(id_num, x_in, nodiabetico, prediabetico, diabetico) 

                results.append([id_num, nodiabetico, prediabetico, diabetico])

        st.markdown("##### PASO 2: visualización de resultados")

        st.markdown(
        """
        Se procede a visualizar los resultados generados en el paso anterior.
        """
        )

        df = pd.DataFrame(
            results,
            columns=['Numero ID', 'NO DIABÉTICO', 'PRE DIABÉTICO', 'DIABÉTICO']
        )
        st.dataframe(df)


    html = """
    <div style="color: lightgray;">
        Created by <a href="https://www.linkedin.com/in/diego-rivera-ai/" 
        style="color: lightgray; !important; text-decoration: none !important;">Diego Rivera</a>
    </div>
    """
    st.markdown(html, unsafe_allow_html=True)
  



if __name__ == '__main__':
    st.set_page_config(
        page_title="Test por lotes",
        page_icon="👋",
    )

    prediction_lote()

import streamlit as st
import pandas as pd
from process import *

from pyecharts import options as opts
from pyecharts.charts import Bar
from streamlit_echarts import st_pyecharts




def prediction_lote():  
    # Título
    html_temp = """
    <h1 style="color:#181082;text-align:center;">Test de diabetes por lotes de pacientes</h1>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    st.markdown(
    """
    Para facilidad se va a cargar un archivo excel previamente construido con datos 
    de pacientes, para hacer una prueba por lotes de sistema en cuanto a su funcionamiento.

    
    

    """
    )

    



if __name__ == '__main__':
    st.set_page_config(
        page_title="Test por lotes",
        page_icon="👋",
    )

    prediction_lote()
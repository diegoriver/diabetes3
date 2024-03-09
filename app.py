import streamlit as st

st.set_page_config(
    page_title="Inicio",
    page_icon="👋",
)

html_temp = """
    <h1 style="color:#181082;text-align:center;">SISTEMA DE PREDICCIÓN DE DIABETES CON UNA RED NEURONAL PROFUNDA</h1>
    </div>
    """
st.markdown(html_temp, unsafe_allow_html=True)


st.markdown(
    """
    Sistema de predicción de diabetes se puede desarrollar de manera individual por cada paciente 
    o procesando un lote de pacientes.
"""
)
 
    
    
    

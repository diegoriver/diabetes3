import streamlit as st
import pandas as pd
from functions import *

from pyecharts import options as opts
from pyecharts.charts import Bar
from streamlit_echarts import st_pyecharts




def prediction():  
    # Título
    html_temp = """
    <h1 style="color:#181082;text-align:center;">Test de diabetes para un paciente</h1>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    st.markdown(
    """
        Se debe seleccionar los datos del formulario siguiente para verificar el funcionamiento 
        del sistema de prediccion de la red neuronal.
        Al final se visualizan los resultados. 
    """
    )

    ### se crea el formulario con Streamlit para la entrada de datos
    # Lecctura de datos
    id_num = st.text_input("Ingrese el ID del paciente (cambie el valor por defecto)", value="123456")

    HighBP_formulario = st.radio("1.Presión Alta:",('Sin presion Alta', 'Con presión Alta'))
    if HighBP_formulario == 'Sin presion Alta': HighBP = 0
    else: HighBP = 1
    
    HighChol_formulario = st.radio( "2.Colesterol: ",('Sin colesterol alto', 'Con colesterol Alto'))
    if HighChol_formulario == 'Sin colesterol alto': HighChol = 0
    else: HighChol = 1

    CholCheck_formulario = st.radio( "3.Chequeo de Colesterol: ",('Ningún control de colesterol en 5 años', 'Control de colesterol en 5 años'))
    if CholCheck_formulario == 'Ningún control de colesterol en 5 años': CholCheck = 0
    else: CholCheck = 1

    BMI = st.slider('4.Indice de Masa Corporal:', 10, 45, 27)

    Smoker_formulario = st.radio( "5.Fumador: ¿Ha fumado al menos 100 cigarrillos en toda su vida? [Nota: 5 paquetes = 100 cigarrillos] ",('No', 'Si'))
    if Smoker_formulario == 'No': Smoker = 0
    else: Smoker = 1

    Stroke_formulario = st.radio( "6.Derrame Cerebral: (Alguna vez te dijeron que tuviste un derrame cerebral.)",('No', 'Si'))
    if Stroke_formulario == 'No': Stroke = 0
    else: Stroke = 1

    HeartDiseaseorAttack_formulario = st.radio( "7.Enfermedad del Corazon: (Enfermedad Coronaria (CHD) o infarto de miocardio (IM))",('No', 'Si'))
    if HeartDiseaseorAttack_formulario == 'No': HeartDiseaseorAttack = 0
    else: HeartDiseaseorAttack = 1

    PhysActivity_formulario = st.radio( "8.Actividad Fisica: (Actividad física en los últimos 30 días - sin incluir el trabajo.)",('No', 'Si'))
    if PhysActivity_formulario == 'No': PhysActivity = 0
    else: PhysActivity = 1

    Fruits_formulario = st.radio( "9.Consume Frutas: (Consume frutaa 1 o más veces al día?)",('No', 'Si'))
    if Fruits_formulario == 'No': Fruits = 0
    else: Fruits = 1

    Veggies_formulario = st.radio( "10.Consume Verduras: (Consume Verduras 1 o más veces al día?)",('No', 'Si'))
    if Veggies_formulario == 'No': Veggies = 0
    else: Veggies = 1

    HvyAlcoholConsump_formulario = st.radio( "11.Bebedor Empedernido: (Hombres adultos que toman más de 14 bebidas por semana y Mujeres adultas que toman más de 7 bebidas por semana.)",('No', 'Si'))
    if HvyAlcoholConsump_formulario == 'No': HvyAlcoholConsump = 0
    else: HvyAlcoholConsump = 1

    AnyHealthcare_formulario = st.radio( "12.Cobertura en Salud: (Tiene cualquier tipo de cobertura de atención médica, incluido seguro de salud, planes prepagados como HMO, etc.)",('No', 'Si'))
    if AnyHealthcare_formulario == 'No': AnyHealthcare = 0
    else: AnyHealthcare = 1

    NoDocbcCost_formulario = st.radio( "13.Consulta Medica: (¿Hubo un momento en los últimos 12 meses en el que necesitó ver a un médico pero no pudo debido al costo?)",('No', 'Si'))
    if NoDocbcCost_formulario == 'No': NoDocbcCost = 0
    else: NoDocbcCost = 1

    GenHlth_formulario = st.radio( "14.Estado de Salud : (Consideras tu estado de salud)",
    ('Excelente', 'Muy Bueno', 'Bueno', 'Justo', 'Pobre'))
    if GenHlth_formulario == 'Excelente': GenHlth = 1
    if GenHlth_formulario == 'Muy Bueno': GenHlth = 2
    if GenHlth_formulario == 'Bueno': GenHlth = 3
    if GenHlth_formulario == 'Justo': GenHlth = 4
    if GenHlth_formulario == 'Pobre': GenHlth = 5
    
    MentHlth = st.slider('15.Salud Mental : (Durante cuantos dias en el ultimo mes ha sufrido de: Stres,Depresion o Emocion. Escala de 0 a 30)', 0, 30, 12)
    
    PhysHlth = st.slider('16.Salud Fisica: (Durante cuantos dias en el ultimo mes su salud fisica no es buena)', 0, 30, 15)
    
    DiffWalk_formulario = st.radio( "17.Dificultad Para Caminar: ¿Tiene serias dificultades para caminar o subir escaleras?",('No', 'Si'))
    if DiffWalk_formulario == 'No': DiffWalk = 0
    else: DiffWalk = 1

    Sex_formulario = st.radio( "18.Sexo:",('Femenino', 'Masculino'))
    if Sex_formulario == 'Femenino': Sex = 0
    else: Sex = 1
    
    Age_formulario = st.radio( "19.Edad:",('De 18 a 24 años', 'De 25 a 29', 'De 30 a 34', 'De 35 a 39', 'De 40 a 44', 'De 45 a 49', 
    'De 50 a 54','De 55 a 59', 'De 60 a 64', 'De 65 a 69', 'De 70 a 74', 'De 75 a 79', '80 a mas'))
    if Age_formulario == 'De 18 a 24 años': Age = 1
    if Age_formulario == 'De 25 a 29': Age = 2
    if Age_formulario == 'De 30 a 34': Age = 3
    if Age_formulario == 'De 35 a 39': Age = 4
    if Age_formulario == 'De 40 a 44': Age = 5
    if Age_formulario == 'De 45 a 49': Age = 6
    if Age_formulario == 'De 50 a 54': Age = 7
    if Age_formulario == 'De 55 a 59': Age = 8
    if Age_formulario == 'De 60 a 64': Age = 9
    if Age_formulario == 'De 65 a 69': Age = 10
    if Age_formulario == 'De 70 a 74': Age = 11
    if Age_formulario == 'De 75 a 79': Age = 12
    if Age_formulario == '80 a mas': Age = 13

    Education_formulario = st.radio( "20.Nivel de Educacion:",
    ('Nunca asistió a la escuela o solo al jardín de infantes', 
    'Grados 1 a 8 (Primaria)', 
    'Grados 9 a 11 (Alguna escuela secundaria)', 
    'Grado 12 o GED (graduado de la escuela secundaria)',
    'Universidad 1 año a 3 años (Alguna universidad o escuela técnica)', 
    'Universidad 4 años o más (graduado universitario)', 
    ))
    if Education_formulario == 'Nunca asistió a la escuela o solo al jardín de infantes': Education = 1
    if Education_formulario == 'Grados 1 a 8 (Primaria)': Education = 2
    if Education_formulario == 'Grados 9 a 11 (Alguna escuela secundaria)': Education = 3
    if Education_formulario == 'Grado 12 o GED (graduado de la escuela secundaria)': Education = 4
    if Education_formulario == 'Universidad 1 año a 3 años (Alguna universidad o escuela técnica)': Education = 5
    if Education_formulario == 'Universidad 4 años o más (graduado universitario)': Education = 6

    Income_formulario = st.radio( "21.Ingresos - USD: ",
    ('Menos de 10.000', 
    'De 10.000 a 16.000', 
    'De 17.000 a 22.000', 
    'De 23.000 a 28.000',
    'De 29.000 a 35.000', 
    'De 36.000 a 48.000', 
    'De 49.000 a 61.000', 
    'De 62.000 a 75.000'
    ))
    if Income_formulario == 'Menos de 10.000': Income = 1
    if Income_formulario == 'De 10.000 a 16.000': Income = 2
    if Income_formulario == 'De 17.000 a 22.000': Income = 3
    if Income_formulario == 'De 23.000 a 28.000': Income = 4
    if Income_formulario == 'De 29.000 a 35.000': Income = 5
    if Income_formulario == 'De 36.000 a 48.000': Income = 6
    if Income_formulario == 'De 49.000 a 61.000': Income = 7
    if Income_formulario == 'De 62.000 a 75.000': Income = 8


    # El botón predicción se usa para iniciar el procesamiento
    if st.button("Predicción:"):
        id_num = (id_num)
        x_in = [np.float_(HighBP),
                np.float_(HighChol),
                np.float_(CholCheck),
                np.float_(BMI),
                np.float_(Smoker),
                np.float_(Stroke),
                np.float_(HeartDiseaseorAttack),
                np.float_(PhysActivity),
                np.float_(Fruits),
                np.float_(Veggies),
                np.float_(HvyAlcoholConsump),
                np.float_(AnyHealthcare),
                np.float_(NoDocbcCost),
                np.float_(GenHlth),
                np.float_(MentHlth),
                np.float_(PhysHlth),
                np.float_(DiffWalk),
                np.float_(Sex),
                np.float_(Age),
                np.float_(Education),
                np.float_(Income)
                ]
        
        ### PASO 0: se realiza la creación del input
        st.markdown("##### PASO 0: se realiza la creación del input...")
        # se crea un archivo input tipo json como ejercicio 
        # suponiendo que la informacion de los inputs se debe guardar como un historico
        create_input(id_num,x_in)


        ### PASO 1: se realiza la predicción y creacion del output
        st.markdown("##### PASO 1: se realiza la predicción y creacion del output...")
        
        # hace la prediccion
        n, nodiabetico, prediabetico, diabetico = prediction_individual(id_num)
        # crea los resultados de salida
        create_output(id_num, x_in, nodiabetico, prediabetico, diabetico)


        ### PASO 2: se realiza la visualización de los datos
        st.markdown("##### PASO 2: se realiza la visualización de los datos...")

        i = n.index(max(n))
        if i == 0:
            resultado_final = "No diabetico"
        elif i == 1:
            resultado_final = "Pre diabetico"
        elif i == 2:
            resultado_final = "Diabetico"

        st.success(f"{resultado_final}")

        df = pd.DataFrame(
            {
                'Numero ID': f"{id_num}",
                'NO DIABÉTICO': f"{nodiabetico}%",
                'PRE DIABÉTICO': f"{prediabetico}%",
                'DIABÉTICO': f"{diabetico}%"
            }, index=["Resultado"]
        )
        st.dataframe(df)

        
        pie_chart = (
            Bar()
            .add_xaxis(["NO DIABETICO", "PRE DIABÉTICO", "DIABÉTICO"])
            .add_yaxis(
                "", [nodiabetico, prediabetico, diabetico]
            )
            .set_global_opts(
                title_opts=opts.TitleOpts(
                    title=f"Predicción del estado de salud de {id_num}", subtitle="% valores en porcentajes"
                ),
            )
        )
        st_pyecharts(pie_chart)


        html = """
        <div style="color: lightgray;">
            Created by <a href="https://www.linkedin.com/in/diego-rivera-ai/" 
            style="color: lightgray; !important; text-decoration: none !important;">Diego Rivera</a>
        </div>
        """
        st.markdown(html, unsafe_allow_html=True)



if __name__ == '__main__':
    st.set_page_config(
        page_title="Test individual",
        page_icon="👋",
    )

    prediction()
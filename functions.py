import tensorflow as tf
import numpy as np
import json
import pandas as pd

model = tf.keras.models.load_model("models/model_diabetes.h5")


def model_prediction(x_in, model):

    x = np.asarray(x_in).reshape(1, -1)
    preds = model.predict(x)

    return preds


def create_input(id_num,x_in):
    datos_in = {"id": id_num, "valores": x_in}

    with open(f"inputs/{id_num}.json", "w") as archivo_json:
        json.dump(datos_in, archivo_json, indent=4)
    

def load_input(id_num):
    try:
        with open(f"inputs/{id_num}.json", "r") as data_json:
            data = json.load(data_json)
            
    except FileNotFoundError:
        print(f"El archivo {id_num}.json no se encontró.")
        
    return data["valores"]


def prediction_individual(id_num):
    # se carga el input de entrada a evaluar
    data = load_input(id_num)

    # se realiza la predicción
    predict = model_prediction(data, model)

    n = predict[0].ravel().tolist()
    nodiabetico = round(n[0]*100, 2)
    prediabetico = round(n[1]*100, 2)
    diabetico = round(n[2]*100, 2)

    return n, nodiabetico, prediabetico, diabetico


def create_output(id_num,x_in, nodiabetico, prediabetico, diabetico):

    datos_out = {"id": id_num, "valores": x_in, "resultado": [nodiabetico, prediabetico, diabetico] }

    with open(f"outputs/{id_num}.json", "w") as archivo_json:
        json.dump(datos_out, archivo_json, indent=4)


def create_inputs_lote_pacientes():
    ## carga del archivo excel (se asume que es la baase de datos con los valores de los pacientes) 
    ruta_archivo = 'db/datos_pacientes.xlsx'
    df = pd.read_excel(ruta_archivo)

    for numero_inputs, row in df.iterrows():
        id_num = str(int(row.iloc[0]))  # carga el valor de la primera columna el cual es el ID de los usuarios
        x_in = row.iloc[1:].tolist()  # carga el resto de valores de las columnas los cuales son los datos medicos de los usuarios
        create_input(id_num,x_in)

    return numero_inputs


def create_outputs_lote_pacientes(id_num,x_in, nodiabetico, prediabetico, diabetico):

    datos_out = {"id": id_num, "valores": x_in, "resultado": [nodiabetico, prediabetico, diabetico] }

    with open(f"outputs/{id_num}.json", "w") as archivo_json:
        json.dump(datos_out, archivo_json, indent=4)
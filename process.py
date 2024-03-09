import tensorflow as tf
import numpy as np
import json


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


def create_output(id_num,x_in, nodiabetico, prediabetico, diabetico):

    datos_out = {"id": id_num, "valores": x_in, "resultado": [nodiabetico, prediabetico, diabetico] }

    with open(f"outputs/{id_num}.json", "w") as archivo_json:
        json.dump(datos_out, archivo_json, indent=4)



import tensorflow as tf
import numpy as np


model = tf.keras.models.load_model("models/model_diabetes.h5")


def model_prediction(x_in, model):

    x = np.asarray(x_in).reshape(1, -1)
    preds = model.predict(x)

    return preds
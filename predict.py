import numpy as np
from model_loader import model
from utlis import class_name, preprocess_image
from PIL import Image

def predict(image):
    image = preprocess_image(image)
    prediction = model.predict(image)
    prediction_index = np.argmax(prediction[0])
    confidence = float(prediction[0][prediction_index])
    disease = class_name[prediction_index]
    return disease,confidence




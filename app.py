# from __future__ import division, print_function
# # coding=utf-8
# import sys
# import os
# import glob
# import re

import numpy as np
import os


# Keras
from keras.applications.vgg19 import preprocess_input, decode_predictions
from tensorflow.keras.utils import img_to_array, load_img
from keras.models import load_model


# Flask utils
from flask import Flask, redirect, url_for, request, render_template
from werkzeug.utils import secure_filename
# from gevent.pywsgi import WSGIServer

# Define a flask app
app = Flask(__name__)

# Model saved with Keras model.save()
MODEL_PATH = 'best_model.h5'

# Load your trained model
model = load_model(MODEL_PATH)
# model._make_predict_function()          # Necessary
print('Model loaded. Start serving...')

print('Model loaded. Check http://127.0.0.1:5000/')

# Classes
ref = {0: 'Apple___Apple_scab',
 1: 'Apple___Black_rot',
 2: 'Apple___Cedar_apple_rust',
 3: 'Apple___healthy',
 4: 'Blueberry___healthy',
 5: 'Cherry_(including_sour)___Powdery_mildew',
 6: 'Cherry_(including_sour)___healthy',
 7: 'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot',
 8: 'Corn_(maize)___Common_rust_',
 9: 'Corn_(maize)___Northern_Leaf_Blight',
 10: 'Corn_(maize)___healthy',
 11: 'Grape___Black_rot',
 12: 'Grape___Esca_(Black_Measles)',
 13: 'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)',
 14: 'Grape___healthy',
 15: 'Orange___Haunglongbing_(Citrus_greening)',
 16: 'Peach___Bacterial_spot',
 17: 'Peach___healthy',
 18: 'Pepper,_bell___Bacterial_spot',
 19: 'Pepper,_bell___healthy',
 20: 'Potato___Early_blight',
 21: 'Potato___Late_blight',
 22: 'Potato___healthy',
 23: 'Raspberry___healthy',
 24: 'Soybean___healthy',
 25: 'Squash___Powdery_mildew',
 26: 'Strawberry___Leaf_scorch',
 27: 'Strawberry___healthy',
 28: 'Tomato___Bacterial_spot',
 29: 'Tomato___Early_blight',
 30: 'Tomato___Late_blight',
 31: 'Tomato___Leaf_Mold',
 32: 'Tomato___Septoria_leaf_spot',
 33: 'Tomato___Spider_mites Two-spotted_spider_mite',
 34: 'Tomato___Target_Spot',
 35: 'Tomato___Tomato_Yellow_Leaf_Curl_Virus',
 36: 'Tomato___Tomato_mosaic_virus',
 37: 'Tomato___healthy'}


def model_predict(img_path, model):
    img = load_img(img_path, target_size=(256, 256))
    i = img_to_array(img)

    im = preprocess_input(i)

    # print(im) #shows array
    # print(im.shape) #shows shape

    img = np.expand_dims(im, axis=0)

    # print(img.shape)

    pred = np.argmax(model.predict(img))
    return pred


@app.route('/', methods=['GET'])
def index():
    # Main page
    return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # Get the file from post request
        f = request.files['file']

        # Save the file to ./uploads
        basepath = os.path.dirname(__file__)
        file_path = os.path.join(secure_filename(f.filename))
        f.save(file_path)

        # Make prediction
        pred = model_predict(file_path, model)
        
        os.remove(file_path)
        # Process your result for human
        # # pred_class = preds.argmax(axis=-1)            # Simple argmax
        # pred_class = decode_predictions(preds, top=1)   # ImageNet Decode
        # result = str(pred_class[0][0][1])               # Convert to string


        result = [f"The detected disease is {ref[pred]} ", f"Apple Cedar apple rust is a fungal disease that affects apple trees, causing yellow-orange spots on leaves, as well as brown or black spots on fruit. It is caused by the fungus Gymnosporangium juniperi-virginianae and is often found on trees near juniper plants."]
        return result
    return None


# For production environment
from gevent import pywsgi
if __name__ == '__main__':
    # Uncomment when going for production
    server = pywsgi.WSGIServer(('0.0.0.0', 5000), app)
    server.serve_forever()

    # app.run(debug=True)
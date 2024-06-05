from flask import Flask, request, jsonify
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import io
from PIL import Image

app = Flask(__name__)

model = load_model('keras_model.h5', compile=False)

class_labels = {0: 'plastico', 1: 'limpo'}

def prepare_image(img):
    img = img.resize((224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = img_array / 255.0
    return img_array

@app.route('/predict', methods=['POST'])
def predict():
    if 'image' not in request.files:
        return jsonify({'error': 'No image part'}), 400

    file = request.files['image']

    if file.filename == '':
        return jsonify({'error': 'No selected image'}), 400

    try:
        img = Image.open(file.stream)
        img_array = prepare_image(img)
    except Exception as e:
        return jsonify({'error': 'Invalid image format'}), 400

    prediction = model.predict(img_array)
    predicted_class = np.argmax(prediction, axis=1)[0]
    label = class_labels[predicted_class]

    return jsonify({'prediction': label})

if __name__ == '__main__':
    app.run(debug=True)
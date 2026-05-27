# main.py
from flask import Flask, request, jsonify
from flask_cors import CORS
import tensorflow as tf
from PIL import Image
import numpy as np
import io

app = Flask(__name__)
CORS(app)  # Allows your HTML page to securely talk to this API

# Load your newly trained model
MODEL = tf.keras.models.load_model('crop_disease_model.h5')

# The exact 38 classes matching your dataset structure
CLASS_NAMES = [
    "Apple___Apple_scab", "Apple___Black_rot", "Apple___Cedar_apple_rust", "Apple___healthy",
    "Blueberry___healthy", "Cherry___Powdery_mildew", "Cherry___healthy", 
    "Corn___Cercospora_leaf_spot", "Corn___Common_rust", "Corn___Northern_Leaf_Blight", "Corn___healthy",
    "Grape___Black_rot", "Grape___Esca_(Black_Measles)", "Grape___Leaf_blight_(Isariopsis_Leaf_Spot)", "Grape___healthy",
    "Orange___Haunglongbing_(Citrus_greening)", "Peach___Bacterial_spot", "Peach___healthy",
    "Pepper,_bell___Bacterial_spot", "Pepper,_bell___healthy", "Potato___Early_blight", "Potato___Late_blight", "Potato___healthy",
    "Raspberry___healthy", "Soybean___healthy", "Squash___Powdery_mildew", "Strawberry___Leaf_scorch", "Strawberry___healthy",
    "Tomato___Bacterial_spot", "Tomato___Early_blight", "Tomato___Late_blight", "Tomato___Leaf_Mold",
    "Tomato___Septoria_leaf_spot", "Tomato___Spider_mites_Two-spotted_spider_mite", "Tomato___Target_Spot",
    "Tomato___Yellow_Leaf_Curl_Virus", "Tomato___Tomato_mosaic_virus", "Tomato___healthy"
]

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400
        
    file = request.files['file']
    try:
        # Open image and convert to RGB array matching model criteria
        image = Image.open(io.BytesIO(file.read())).convert('RGB')
        image = image.resize((224, 224))
        img_array = np.array(image) / 255.0
        img_array = np.expand_dims(img_array, axis=0)
        
        # Run calculation
        predictions = MODEL.predict(img_array)
        predicted_class_idx = np.argmax(predictions[0])
        confidence = float(np.max(predictions[0])) * 100
        
        raw_name = CLASS_NAMES[predicted_class_idx]
        clean_name = raw_name.replace("___", " - ").replace("_", " ")
        
        return jsonify({
            'disease': clean_name,
            'confidence': f"{confidence:.2f}%"
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
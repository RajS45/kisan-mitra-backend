# predict_utils.py
import cv2
import numpy as np
import tensorflow as tf
import config

def load_labels():
    """Loads class labels from text file."""
    with open(config.LABELS_PATH, 'r') as f:
        labels = [line.strip() for line in f.readlines()]
    return labels

def predict_crop_disease(image_path_or_bytes):
    """Takes image path/bytes, runs preprocessing, and extracts disease predictions."""
    # Handle both file paths and memory buffers (Streamlit uses bytes)
    if isinstance(image_path_or_bytes, str):
        img = cv2.imread(image_path_or_bytes)
    else:
        file_bytes = np.frombuffer(image_path_or_bytes.read(), np.uint8)
        img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
        
    # Preprocess
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img_resized = cv2.resize(img, config.IMG_SIZE)
    img_array = np.expand_dims(img_resized, axis=0) / 255.0

    # Inference
    model = tf.keras.models.load_model(config.MODEL_PATH)
    predictions = model.predict(img_array)
    
    # Process confidence metrics
    class_labels = load_labels()
    highest_idx = np.argmax(predictions[0])
    confidence = predictions[0][highest_idx]
    predicted_disease = class_labels[highest_idx]
    
    return predicted_disease, confidence
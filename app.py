# app.py
import streamlit as st
from PIL import Image
import os
import config
from prediction_utils import predict_crop_disease
st.set_page_config(page_title="Crop Disease Diagnostic Lab", layout="centered")

st.title("🌱 Crop Disease Diagnostic Assistant")
st.write("Upload a clear photo of a plant leaf to analyze it for possible diseases or deficiencies.")

# Error check to verify model existence before running
if not os.path.exists(config.MODEL_PATH):
    st.error(f"Model file '{config.MODEL_PATH}' not found. Please run 'python train.py' first.")
else:
    uploaded_file = st.file_uploader("Choose a leaf image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Display User Image
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Sample Leaf Layer', use_container_width=True)
        
        st.write("🔄 *Analyzing patterns...*")
        
        # Reset file pointer and predict
        uploaded_file.seek(0)
        disease, confidence = predict_crop_disease(uploaded_file)
        
        # UI Presentation Metrics
        st.subheader("Diagnostic Assessment Summary")
        if "healthy" in disease.lower():
            st.success(f"**Result**: The crop leaf appears to be **{disease.replace('_', ' ')}**")
        else:
            st.warning(f"**Detected Abnormality**: **{disease.replace('_', ' ')}**")
            
        st.metric(label="System Predictive Confidence Score", value=f"{confidence * 100:.2f}%")
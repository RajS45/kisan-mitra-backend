# config.py
import os

# Image configurations
IMG_SIZE = (224, 224)
INPUT_SHAPE = (224, 224, 3)
BATCH_SIZE = 32
EPOCHS = 10

# --- USE EXACT PATHS TO FIX THE VALUEERROR ---
# This points exactly to where your dataset folder is located on your Desktop
BASE_DIR = r"C:\Users\raj23\OneDrive\Desktop\pythonPlace\crop_disease_project\dataset"

TRAIN_DIR = os.path.join(BASE_DIR, 'train')
VAL_DIR = os.path.join(BASE_DIR, 'validation')
MODEL_PATH = os.path.join(r"C:\Users\raj23\OneDrive\Desktop\pythonPlace\crop_disease_project", 'crop_disease_model.h5')
LABELS_PATH = os.path.join(r"C:\Users\raj23\OneDrive\Desktop\pythonPlace\crop_disease_project", 'class_labels.txt')
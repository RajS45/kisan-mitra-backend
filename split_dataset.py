# split_dataset.py
import os
import shutil
from sklearn.model_selection import train_test_split

# 1. CHANGE THIS PATH to the exact folder where you extracted your new dataset zip!
RAW_DATA_DIR = r"C:\Users\raj23\Downloads\archive\plantvillage dataset\color" 

TARGET_DIR = "dataset"

# Create target directories if they don't exist
for split in ['train', 'validation']:
    os.makedirs(os.path.join(TARGET_DIR, split), exist_ok=True)

print("Scanning folders and splitting data... Please wait.")

# Loop through and split every category folder
for category in os.listdir(RAW_DATA_DIR):
    category_path = os.path.join(RAW_DATA_DIR, category)
    
    if os.path.isdir(category_path):
        # Grab all image files
        images = [f for f in os.listdir(category_path) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
        if len(images) == 0:
            continue
            
        # 80% train, 20% validation split
        train_imgs, val_imgs = train_test_split(images, test_size=0.2, random_state=42)
        
        # Create subfolders inside dataset/train and dataset/validation
        os.makedirs(os.path.join(TARGET_DIR, 'train', category), exist_ok=True)
        os.makedirs(os.path.join(TARGET_DIR, 'validation', category), exist_ok=True)
        
        # Copy the files over
        for img in train_imgs:
            shutil.copy(os.path.join(category_path, img), os.path.join(TARGET_DIR, 'train', category, img))
        for img in val_imgs:
            shutil.copy(os.path.join(category_path, img), os.path.join(TARGET_DIR, 'validation', category, img))

print("🎉 Success! Your dataset folder is now perfectly split into train and validation sets.")
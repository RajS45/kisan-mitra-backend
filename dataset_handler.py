# dataset_handler.py
import tensorflow as tf
import os
import config

def get_data_generators():
    """Loads images using the modern, high-performance tf.data pipeline."""
    
    # Load Training Dataset
    train_ds = tf.keras.utils.image_dataset_from_directory(
        config.TRAIN_DIR,
        image_size=config.IMG_SIZE,
        batch_size=config.BATCH_SIZE,
        label_mode='categorical',
        shuffle=True
    )

    # Load Validation Dataset
    val_ds = tf.keras.utils.image_dataset_from_directory(
        config.VAL_DIR,
        image_size=config.IMG_SIZE,
        batch_size=config.BATCH_SIZE,
        label_mode='categorical',
        shuffle=False
    )
    
    # Extract text labels and save them to a file for the Streamlit App
    labels = train_ds.class_names
    with open(config.LABELS_PATH, 'w') as f:
        for label in labels:
            f.write(f"{label}\n")

    # Prefetch data into memory to speed up hardware training cycles
    train_ds = train_ds.prefetch(buffer_size=tf.data.AUTOTUNE)
    val_ds = val_ds.prefetch(buffer_size=tf.data.AUTOTUNE)

    return train_ds, val_ds
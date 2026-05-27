# train.py
import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.applications import MobileNetV2
import config
from dataset_handler import get_data_generators

def build_model(num_classes):
    """Builds a model with embedded rescaling and data augmentation layers."""
    
    # Embedded Augmentation Pipeline
    data_augmentation = models.Sequential([
        layers.RandomFlip("horizontal"),
        layers.RandomRotation(0.2),
        layers.RandomZoom(0.2),
    ])

    # MobileNetV2 expects values scaled between -1 and 1 or 0 and 1.
    # We embed rescaling directly inside the architecture layer layout.
    rescaling = layers.Rescaling(1./255)

    base_model = MobileNetV2(weights='imagenet', include_top=False, input_shape=config.INPUT_SHAPE)
    base_model.trainable = False  # Freeze backbone pre-trained weights

    # Sequence everything together
    inputs = layers.Input(shape=config.INPUT_SHAPE)
    x = data_augmentation(inputs)
    x = rescaling(x)
    x = base_model(x, training=False)
    x = layers.GlobalAveragePooling2D()(x)
    x = layers.Dense(128, activation='relu')(x)
    x = layers.Dropout(0.3)(x)
    outputs = layers.Dense(num_classes, activation='softmax')(x)
    
    model = models.Model(inputs, outputs)
    
    model.compile(
        optimizer='adam',
        loss='categorical_crossentropy',
        metrics=['accuracy']
    )
    return model

if __name__ == "__main__":
    print("Initializing Modern Data Pipelines...")
    train_ds, val_ds = get_data_generators()
    
    # Read text labels metadata file to find the number of categories
    with open(config.LABELS_PATH, 'r') as f:
        num_classes = len(f.readlines())

    print(f"Building Model for {num_classes} classes...")
    model = build_model(num_classes)

    print("Starting Model Training...")
    history = model.fit(
        train_ds,
        validation_data=val_ds,
        epochs=config.EPOCHS
    )

    print(f"Saving trained model to {config.MODEL_PATH}...")
    model.save(config.MODEL_PATH)
    print("Training completed successfully!")
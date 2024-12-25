import tensorflow as tf
import numpy as np
from PIL import Image
import os

# Class labels
class_labels = ["Bacterial Wilt Disease", "Healthy", "Manganese Toxicity"]

def load_models():
    """Load VGG16 and VGG19 models from disk."""
    try:
        # Flexible path handling for model files
        base_path = "C:/Users/taris/Documents/SEM 7/ML/UAP/src/uap/model"
        vgg16_model = tf.keras.models.load_model(os.path.join(base_path, 'vgg16_model.keras'))
        vgg19_model = tf.keras.models.load_model(os.path.join(base_path, 'vgg19_model.keras'))
        return vgg16_model, vgg19_model
    except Exception as e:
        raise RuntimeError(f"Error loading models: {str(e)}")

def is_valid_image(image):
    """Check if the uploaded image is valid."""
    # Ensure image has color channels (RGB or RGBA)
    if image.mode not in ('RGB', 'RGBA'):
        return False
    return True

def predict(image, model):
    """Predict the class of the uploaded image using the selected model."""
    try:
        # Validate the image
        if not is_valid_image(image):
            raise ValueError("Invalid image format. Please upload RGB or RGBA images.")

        # Preprocess the image
        image = image.resize((224, 224))  # Resize to the input size of the model
        image = np.array(image) / 255.0  # Normalize the image
        image = np.expand_dims(image, axis=0)  # Add batch dimension

        # Perform prediction
        predictions = model.predict(image)

        # Ensure predictions are a numpy array
        predictions = np.array(predictions).flatten()
        
        return predictions  # Return probabilities directly
    except Exception as e:
        return np.array([]), f"Error: {str(e)}"
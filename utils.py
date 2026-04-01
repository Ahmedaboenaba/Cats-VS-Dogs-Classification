"""
Utility module for Cats vs Dogs classification inference

This module provides helper functions for:
- Loading the trained model
- Making predictions on images
- Batch processing
- Exporting predictions

Usage:
    from utils import CatsDogsClassifier

    classifier = CatsDogsClassifier()
    label, confidence = classifier.predict('image.jpg')
"""

import os
import numpy as np
from PIL import Image
from pathlib import Path
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
from typing import Tuple, List, Dict
import json
from datetime import datetime


class CatsDogsClassifier:
    """
    Production-ready classifier for cats vs dogs images
    """

    def __init__(self, model_path: str = "./models/cats_dogs_cnn_model.keras"):
        """
        Initialize the classifier

        Args:
            model_path: Path to the trained model
        """
        self.model_path = model_path
        self.model = None
        self.image_size = (128, 128)
        self.class_names = ['Cat', 'Dog']
        self.load_model()

    def load_model(self) -> bool:
        """
        Load the trained model

        Returns:
            bool: True if successful, False otherwise
        """
        try:
            # Try primary format
            if os.path.exists(self.model_path):
                self.model = load_model(self.model_path)
                print(f"✓ Model loaded from: {self.model_path}")
                return True

            # Try alternative format
            alt_path = self.model_path.replace('.keras', '.h5')
            if os.path.exists(alt_path):
                self.model = load_model(alt_path)
                print(f"✓ Model loaded from: {alt_path}")
                return True

            print(f"✗ Model not found at {self.model_path}")
            return False

        except Exception as e:
            print(f"✗ Error loading model: {e}")
            return False

    def _preprocess_image(self, image: Image.Image) -> np.ndarray:
        """
        Preprocess image for model prediction

        Args:
            image: PIL Image object

        Returns:
            np.ndarray: Preprocessed image batch
        """
        # Resize
        image = image.resize(self.image_size)

        # Convert to array
        img_array = img_to_array(image)

        # Normalize (0-1 range)
        img_array = img_array / 255.0

        # Add batch dimension
        img_batch = np.expand_dims(img_array, axis=0)

        return img_batch

    def predict(self, image_path: str) -> Tuple[str, float]:
        """
        Make prediction on a single image

        Args:
            image_path: Path to image file

        Returns:
            Tuple: (prediction_label, confidence_score)
        """
        if self.model is None:
            print("✗ Model not loaded")
            return None, None

        try:
            # Load image
            if isinstance(image_path, str):
                image = Image.open(image_path).convert('RGB')
            else:
                image = image_path.convert('RGB')

            # Preprocess
            img_batch = self._preprocess_image(image)

            # Predict
            prediction = self.model.predict(img_batch, verbose=0)[0][0]

            # Interpret
            label = self.class_names[1] if prediction > 0.5 else self.class_names[0]
            confidence = prediction if prediction > 0.5 else (1 - prediction)

            return label, float(confidence)

        except Exception as e:
            print(f"✗ Error during prediction: {e}")
            return None, None

    def predict_batch(self, image_paths: List[str]) -> List[Dict]:
        """
        Make predictions on multiple images

        Args:
            image_paths: List of image file paths

        Returns:
            List[Dict]: List of predictions with metadata
        """
        results = []

        for image_path in image_paths:
            label, confidence = self.predict(image_path)

            results.append({
                'image': image_path,
                'prediction': label,
                'confidence': confidence,
                'timestamp': datetime.now().isoformat()
            })

        return results

    def predict_directory(self, directory: str) -> List[Dict]:
        """
        Make predictions on all images in a directory

        Args:
            directory: Path to directory containing images

        Returns:
            List[Dict]: List of predictions
        """
        supported_formats = ('.jpg', '.jpeg', '.png', '.JPG', '.PNG')
        image_paths = []

        # Find all image files
        for root, dirs, files in os.walk(directory):
            for file in files:
                if file.endswith(supported_formats):
                    image_paths.append(os.path.join(root, file))

        print(f"Found {len(image_paths)} images. Processing...")
        return self.predict_batch(image_paths)

    def save_predictions(self, predictions: List[Dict], output_file: str = 'predictions.json'):
        """
        Save predictions to JSON file

        Args:
            predictions: List of prediction results
            output_file: Output file path
        """
        try:
            with open(output_file, 'w') as f:
                json.dump(predictions, f, indent=2)
            print(f"✓ Predictions saved to: {output_file}")
        except Exception as e:
            print(f"✗ Error saving predictions: {e}")

    def get_model_info(self) -> Dict:
        """Get information about the loaded model"""
        if self.model is None:
            return {'error': 'Model not loaded'}

        return {
            'input_shape': self.model.input_shape,
            'output_shape': self.model.output_shape,
            'total_parameters': self.model.count_params(),
            'layers': len(self.model.layers),
            'class_names': self.class_names
        }


# =====================
# CONVENIENCE FUNCTIONS
# =====================

def quick_predict(image_path: str, model_path: str = "./models/cats_dogs_cnn_model.keras") -> Tuple[str, float]:
    """
    Quick prediction without creating classifier instance

    Usage:
        label, conf = quick_predict('image.jpg')
        print(f"Prediction: {label} ({conf:.1%})")
    """
    classifier = CatsDogsClassifier(model_path)
    return classifier.predict(image_path)


def batch_predict(directory: str, model_path: str = "./models/cats_dogs_cnn_model.keras") -> List[Dict]:
    """
    Batch predict directory without creating classifier instance

    Usage:
        results = batch_predict('./my_images/')
        for result in results:
            print(f"{result['image']}: {result['prediction']}")
    """
    classifier = CatsDogsClassifier(model_path)
    return classifier.predict_directory(directory)


# =====================
# EXAMPLE USAGE
# =====================

if __name__ == '__main__':
    print("="*60)
    print("🐱🐶 Cats vs Dogs Classifier - Utility Module")
    print("="*60)

    # Example 1: Single image prediction
    print("\n📌 Example 1: Single Image Prediction")
    print("-" * 60)
    print("""
    from utils import quick_predict

    label, confidence = quick_predict('cat.jpg')
    print(f"Prediction: {label} ({confidence:.1%})")
    """)

    # Example 2: Batch processing
    print("\n📌 Example 2: Batch Processing")
    print("-" * 60)
    print("""
    from utils import CatsDogsClassifier

    classifier = CatsDogsClassifier()
    results = classifier.predict_directory('./test_images/')

    for result in results:
        print(f"  {result['image']}: {result['prediction']} ({result['confidence']:.1%})")
    """)

    # Example 3: With model info
    print("\n📌 Example 3: Model Information")
    print("-" * 60)
    print("""
    from utils import CatsDogsClassifier

    classifier = CatsDogsClassifier()
    info = classifier.get_model_info()
    print(f"Model Parameters: {info['total_parameters']:,}")
    print(f"Input Shape: {info['input_shape']}")
    """)

    print("\n" + "="*60)

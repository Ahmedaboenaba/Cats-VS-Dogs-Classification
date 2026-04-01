"""
Cats vs Dogs Classification - Flask Web Application (Alternative)

A Flask-based web app for cats vs dogs classification.

Setup:
    pip install flask pillow tensorflow numpy

Run with:
    python app_flask.py

Then visit: http://localhost:5000
"""

from flask import Flask, render_template, request, jsonify
from PIL import Image
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
import numpy as np
import os
from io import BytesIO
import base64

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

# Model configuration
MODEL_PATH = "cats_dogs_cnn_model.keras"
ALT_MODEL_PATH = "./models/cats_dogs_cnn_model.h5"
IMAGE_SIZE = (128, 128)

# Load model
model = None
model_loaded = False

def load_trained_model():
    """Load the trained CNN model"""
    global model, model_loaded
    try:
        if os.path.exists(MODEL_PATH):
            model = load_model(MODEL_PATH)
        elif os.path.exists(ALT_MODEL_PATH):
            model = load_model(ALT_MODEL_PATH)
        else:
            print(f"Warning: Model not found at {MODEL_PATH} or {ALT_MODEL_PATH}")
            model_loaded = False
            return
        model_loaded = True
        print("✓ Model loaded successfully")
    except Exception as e:
        print(f"Error loading model: {e}")
        model_loaded = False

def preprocess_image(image):
    """Preprocess image for prediction"""
    image = image.resize(IMAGE_SIZE)
    img_array = img_to_array(image) / 255.0
    img_batch = np.expand_dims(img_array, axis=0)
    return img_batch

def predict_image(image):
    """
    Make prediction on image
    Returns: (label, confidence)
    """
    if model is None or not model_loaded:
        return None, None

    try:
        img_batch = preprocess_image(image)
        prediction = model.predict(img_batch, verbose=0)[0][0]

        label = "Dog" if prediction > 0.5 else "Cat"
        confidence = prediction if prediction > 0.5 else (1 - prediction)

        return label, float(confidence)
    except Exception as e:
        print(f"Prediction error: {e}")
        return None, None

@app.route('/')
def index():
    """Serve the main page"""
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    """Handle image prediction"""
    if not model_loaded:
        return jsonify({
            'error': 'Model not loaded. Ensure model file exists at ./models/',
            'success': False
        }), 500

    try:
        # Check if image was provided
        if 'file' not in request.files:
            return jsonify({'error': 'No image provided', 'success': False}), 400

        file = request.files['file']

        if file.filename == '':
            return jsonify({'error': 'No file selected', 'success': False}), 400

        # Check file type
        allowed_extensions = {'.jpg', '.jpeg', '.png'}
        file_ext = os.path.splitext(file.filename)[1].lower()
        if file_ext not in allowed_extensions:
            return jsonify({'error': 'Invalid file type. Use JPG or PNG.', 'success': False}), 400

        # Load and process image
        image = Image.open(file.stream).convert('RGB')

        # Make prediction
        label, confidence = predict_image(image)

        if label is None:
            return jsonify({'error': 'Prediction failed', 'success': False}), 500

        # Convert image to base64 for display
        buffered = BytesIO()
        image.save(buffered, format="PNG")
        img_base64 = base64.b64encode(buffered.getvalue()).decode()

        return jsonify({
            'success': True,
            'prediction': label,
            'confidence': f"{confidence:.1%}",
            'confidence_score': float(confidence),
            'image': f"data:image/png;base64,{img_base64}"
        })

    except Exception as e:
        return jsonify({'error': str(e), 'success': False}), 500

@app.route('/health')
def health():
    """Health check endpoint"""
    return jsonify({
        'status': 'online',
        'model_loaded': model_loaded,
        'model_path': MODEL_PATH
    })

if __name__ == '__main__':
    # Load model on startup
    print("Loading model...")
    load_trained_model()

    print("\n" + "="*50)
    print("🐱 Cats vs Dogs Classifier - Flask")
    print("="*50)
    print("\nStarting server...")
    print("Visit: http://localhost:5000")
    print("\nPress CTRL+C to stop")
    print("="*50 + "\n")

    # Run Flask app
    app.run(debug=True, host='0.0.0.0', port=5000)

"""
Cats vs Dogs Classification - Streamlit Web Application

A simple, user-friendly web app to classify images of cats and dogs
using a pre-trained CNN model.

Run with: streamlit run app.py
"""
import streamlit as st
import numpy as np
from PIL import Image
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
import os

# Page config
st.set_page_config(
    page_title="Cats vs Dogs Classifier",
    page_icon="🐱🐶",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main {
        padding: 2rem;
    }
    .prediction-box {
        padding: 1.5rem;
        border-radius: 10px;
        margin: 1rem 0;
    }
    .cat {
        background-color: #FFE5CC;
        border: 2px solid #FF9800;
    }
    .dog {
        background-color: #E3F2FD;
        border: 2px solid #2196F3;
    }
</style>
""", unsafe_allow_html=True)

class CatsDogsClassifier:
    """Helper class for model loading and predictions"""

    def __init__(self, model_path="cats_dogs_cnn_model.keras"):
        self.model_path = model_path
        self.model = None
        self.image_size = (128, 128)
        self.load_model()

    def load_model(self):
        """Load the trained model"""
        try:
            # Try loading as .keras format first
            if os.path.exists(self.model_path):
                self.model = load_model(self.model_path)
            # Fall back to .h5 format
            elif os.path.exists(self.model_path.replace('.keras', '.h5')):
                self.model = load_model(self.model_path.replace('.keras', '.h5'))
            else:
                return False
            return True
        except Exception as e:
            st.error(f"Error loading model: {e}")
            return False

    def preprocess_image(self, image):
        """Preprocess image for model prediction"""
        # Resize image
        image = image.resize(self.image_size)
        # Convert to array and normalize
        img_array = img_to_array(image) / 255.0
        # Add batch dimension
        img_batch = np.expand_dims(img_array, axis=0)
        return img_batch

    def predict(self, image):
        """
        Make prediction on image
        Returns: (label, confidence)
        """
        if self.model is None:
            return None, None

        try:
            # Preprocess image
            img_batch = self.preprocess_image(image)

            # Make prediction
            prediction = self.model.predict(img_batch, verbose=0)[0][0]

            # Interpret result (0 = Cat, 1 = Dog)
            label = "Dog" if prediction > 0.5 else "Cat"
            confidence = prediction if prediction > 0.5 else (1 - prediction)

            return label, float(confidence)
        except Exception as e:
            st.error(f"Error making prediction: {e}")
            return None, None

# Initialize session state
if 'classifier' not in st.session_state:
    st.session_state.classifier = CatsDogsClassifier()

# UI Layout
st.title("🐱 Cats vs Dogs Classifier 🐶")
st.markdown("### Identify whether an image contains a cat or a dog")

# Sidebar info
with st.sidebar:
    st.header("ℹ️ About")
    st.markdown("""
    This app uses a **Convolutional Neural Network (CNN)**
    trained to classify images of cats and dogs.

    **Model Details:**
    - Architecture: Sequential CNN
    - Input Size: 128×128×3
    - Training Accuracy: ~85%+
    - Framework: TensorFlow/Keras

    **How to use:**
    1. Upload an image (JPG, PNG)
    2. View the prediction
    3. Check the confidence score

    **Supported formats:** JPG, JPEG, PNG
    """)

# Main content
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("📤 Upload Image")
    uploaded_file = st.file_uploader(
        "Choose an image file",
        type=["jpg", "jpeg", "png"],
        help="Upload a clear image of a cat or dog"
    )

with col2:
    st.subheader("📷 Or Capture (Camera)")
    camera_image = st.camera_input("Take a photo")

# Process uploaded file or camera input
image_to_predict = None
image_source = None

if uploaded_file is not None:
    image_to_predict = Image.open(uploaded_file).convert('RGB')
    image_source = "upload"
elif camera_image is not None:
    image_to_predict = Image.open(camera_image).convert('RGB')
    image_source = "camera"

# Display image and make prediction
if image_to_predict is not None:
    col1, col2 = st.columns([1, 1])

    with col1:
        st.image(image_to_predict, caption="Input Image", use_column_width=True)

    with col2:
        st.subheader("🔮 Prediction")

        # Check if model is loaded
        if st.session_state.classifier.model is None:
            st.error("⚠️ Model not loaded. Make sure 'models/cats_dogs_cnn_model.keras' exists.")
        else:
            # Make prediction
            label, confidence = st.session_state.classifier.predict(image_to_predict)

            if label and confidence is not None:
                # Display prediction with styling
                if label == "Cat":
                    css_class = "cat"
                    emoji = "🐱"
                else:
                    css_class = "dog"
                    emoji = "🐶"

                st.markdown(f"""
                <div class="prediction-box {css_class}">
                    <h2>{emoji} {label}</h2>
                    <p><strong>Confidence:</strong> {confidence:.1%}</p>
                </div>
                """, unsafe_allow_html=True)

                # Confidence bar
                st.progress(confidence, text=f"Confidence: {confidence:.1%}")

                # Explanation
                if confidence > 0.8:
                    st.success(f"✓ High confidence this is a {label.lower()}")
                elif confidence > 0.6:
                    st.info(f"~ Medium confidence this is a {label.lower()}")
                else:
                    st.warning(f"⚠️ Low confidence in prediction. Image might be unclear or ambiguous.")
            else:
                st.error("Could not make prediction. Please try with a different image.")

# Footer
st.divider()
st.markdown("""
<div style="text-align: center; color: gray; padding: 1rem;">
    <small>Built with Streamlit & TensorFlow</small>
    <br/>
    <small>Model Performance: ~85% accuracy on validation set</small>
</div>
""", unsafe_allow_html=True)

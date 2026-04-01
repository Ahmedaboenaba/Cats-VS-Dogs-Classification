"""
Configuration file for Cats vs Dogs Classification

Customize model parameters, paths, and training settings here.
"""

# =====================
# MODEL PATHS
# =====================
MODEL_PATH = "./models/cats_dogs_cnn_model.keras"
ALT_MODEL_PATH = "./models/cats_dogs_cnn_model.h5"
DATASET_PATH = "./dataset"

# =====================
# IMAGE SETTINGS
# =====================
IMAGE_SIZE = (128, 128)  # Target image size
IMAGE_CHANNELS = 3  # RGB
SUPPORTED_FORMATS = ['.jpg', '.jpeg', '.png']

# =====================
# TRAINING PARAMETERS
# =====================
BATCH_SIZE = 32
EPOCHS = 10
VALIDATION_SPLIT = 0.2
RANDOM_SEED = 42

# =====================
# OPTIMIZER SETTINGS
# =====================
LEARNING_RATE = 0.001
OPTIMIZER = 'adam'
LOSS_FUNCTION = 'binary_crossentropy'
METRICS = ['accuracy']

# =====================
# DATA AUGMENTATION
# =====================
DATA_AUGMENTATION = {
    'rotation_range': 20,
    'width_shift_range': 0.2,
    'height_shift_range': 0.2,
    'shear_range': 0.2,
    'zoom_range': 0.2,
    'horizontal_flip': True,
}

# =====================
# PREDICTION SETTINGS
# =====================
CONFIDENCE_THRESHOLD = 0.5  # 0.5 for binary classification
CLASS_NAMES = ['Cat', 'Dog']
PREDICTION_CONFIDENCE_FORMAT = "percentage"  # or "fraction"

# =====================
# WEB APP SETTINGS
# =====================
APP_PORT = 5000
APP_HOST = '0.0.0.0'
APP_DEBUG = True
MAX_FILE_SIZE = 16 * 1024 * 1024  # 16 MB

# Streamlit settings
STREAMLIT_PORT = 8501

# =====================
# LOGGING
# =====================
LOG_LEVEL = "INFO"  # DEBUG, INFO, WARNING, ERROR
LOG_FILE = "./logs/app.log"

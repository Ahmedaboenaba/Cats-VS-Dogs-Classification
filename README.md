# Cats vs Dogs Binary Image Classification with CNN

A complete, production-ready deep learning pipeline for classifying images of cats and dogs using a Convolutional Neural Network (CNN).

## 📋 Contents

- Complete Jupyter Notebook with full training pipeline
- Streamlit web application (recommended for deployment)
- Flask web application (alternative)
- Pre-trained model
- Setup and deployment instructions

## 🎯 Project Structure

```
.
├── cats_Vs_Dogs CNN.ipynb          # Main Jupyter Notebook
├── app.py                           # Streamlit deployment app
├── app_flask.py                     # Flask deployment app
├── templates/
│   └── index.html                   # Flask HTML template
├── models/
│   ├── cats_dogs_cnn_model.h5      # Trained model (HDF5)
│   └── cats_dogs_cnn_model.keras   # Trained model (Keras format)
├── dataset/
│   ├── cats/                        # Cat images
│   └── dogs/                        # Dog images
└── requirements.txt                 # Python dependencies
```

## ⚙️ Setup Instructions

### 1. Prerequisites

- Python 3.8+
- pip package manager
- Git (optional)

### 2. Create Virtual Environment (Recommended)

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Prepare Dataset

Organize your cat and dog images in the following structure:

```
dataset/
├── cats/
│   ├── cat1.jpg
│   ├── cat2.jpg
│   └── ...
└── dogs/
    ├── dog1.jpg
    ├── dog2.jpg
    └── ...
```

**Dataset Notes:**
- Recommended: 100+ images per category
- Supported formats: JPG, JPEG, PNG
- Image size: Any size (will be resized to 128×128)

#### Free Datasets:
- **Google Open Images**: https://storage.googleapis.com/openimages/web/index.html
- **Microsoft COCO**: https://cocodataset.org/
- **ImageNet**: https://www.image-net.org/
- **Kaggle Datasets**: https://www.kaggle.com/datasets (search "cats and dogs")

## 🚀 Usage

### Option A: Train & Deploy with Jupyter Notebook

```bash
# Start Jupyter Lab/Notebook
jupyter notebook
```

1. Open `cats_Vs_Dogs CNN.ipynb`
2. Run cells sequentially from top to bottom
3. Trained model will be saved to `./models/`

**Expected Training Time:**
- On CPU: 10-15 minutes
- On GPU: 2-5 minutes

### Option B: Streamlit Deployment (Recommended) 🎯

**Best for:** Easy web interface, quick deployment

```bash
# Install if not already installed
pip install streamlit

# Run the app
streamlit run app.py
```

**Access the app:**
- Local: `http://localhost:8501`
- Features:
  - Drag & drop image upload
  - Real-time predictions
  - Confidence scores
  - Camera input support

### Option C: Flask Deployment (Alternative)

```bash
# Install if not already installed
pip install flask

# Run the Flask app
python app_flask.py
```

**Access the app:**
- Local: `http://localhost:5000`
- Features:
  - Classic web interface
  - Image upload
  - Confidence visualization

## 📊 Model Information

**Architecture:**
- 3 Convolutional blocks (32, 64, 128 filters)
- MaxPooling layers for dimensionality reduction
- Dropout layers for regularization (0.25, 0.5)
- Dense layers (256, 128 units)
- Output: Sigmoid activation for binary classification

**Performance:**
- Expected Accuracy: ~85%+
- Training: 10 epochs
- Optimizer: Adam (learning rate 0.001)
- Loss: Binary Cross-Entropy

**Input:**
- Size: 128×128×3 (RGB)
- Preprocessing: Normalized (0-1 range)

## 📤 Deployment Options

### Local Deployment
Already configured - run Streamlit or Flask app

### Cloud Deployment (Free Tier Options)

#### 1. Streamlit Cloud (Recommended)

**Zero-cost, easiest deployment**

1. Push code to GitHub
2. Go to https://streamlit.io/cloud
3. Click "New app"
4. Select your GitHub repo
5. Deploy in 1 click!

**Free Plan Includes:**
- 5 publicly deployed apps
- Unlimited users
- Automatic updates from GitHub

#### 2. Heroku (Flask)

**Free tier available with limitations**

```bash
# Install Heroku CLI
# https://devcenter.heroku.com/articles/heroku-cli

# Login
heroku login

# Create app
heroku create your-app-name

# Deploy
git push heroku main

# View logs
heroku logs --tail
```

**Note:** Heroku's free tier was discontinued in Nov 2022. Alternatives:
- Render.com (free tier available)
- Fly.io (free tier available)
- Railway.app (free tier available)

#### 3. Google Colab (Free GPU)

```bash
# Upload notebook to Colab
# Run cells with free GPU
# No deployment needed - runs in browser
```

#### 4. Hugging Face Spaces (Free)

1. Create account at https://huggingface.co
2. Create new Space
3. Select Streamlit template
4. Upload `app.py` and model files
5. Deploy automatically!

## 🔄 Making Predictions

### In Notebook
```python
from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np

# Load model
model = load_model('./models/cats_dogs_cnn_model.keras')

# Load image
img = Image.open('path/to/image.jpg').convert('RGB')
img = img.resize((128, 128))
img_array = np.array(img) / 255.0
img_batch = np.expand_dims(img_array, axis=0)

# Predict
prediction = model.predict(img_batch)[0][0]
label = 'Dog' if prediction > 0.5 else 'Cat'
confidence = prediction if prediction > 0.5 else (1 - prediction)

print(f"Prediction: {label}, Confidence: {confidence:.2%}")
```

### Via Web App
1. Open Streamlit/Flask app
2. Upload image
3. Click "Analyze"
4. View prediction instantly

## 🛠️ Troubleshooting

### Issue: Model not found
**Solution:** Train the model in the Jupyter notebook first or download pre-trained model

### Issue: Out of memory
**Solutions:**
- Reduce image size in config
- Reduce batch size
- Use GPU (requires CUDA)

### Issue: Low accuracy
**Solutions:**
- Increase number of epochs (up to 20)
- Collect more training data
- Use data augmentation
- Fine-tune learning rate

### Issue: Streamlit app won't load
**Solution:**
```bash
pip install --upgrade streamlit
```

### Issue: GPU not detected
```bash
# Check TensorFlow GPU
python -c "import tensorflow as tf; print(tf.config.list_physical_devices('GPU'))"

# If empty, reinstall:
pip install tensorflow[and-cuda]
```

## 📈 Model Training Tips

1. **Data Augmentation:** Already included in notebook
   - Rotation, shifts, zoom, flips
   - Prevents overfitting

2. **Transfer Learning Option:**
   ```python
   from tensorflow.keras.applications import MobileNetV2
   base_model = MobileNetV2(input_shape=(128, 128, 3), include_top=False)
   # Add custom head for binary classification
   ```

3. **Early Stopping:**
   ```python
   from tensorflow.keras.callbacks import EarlyStopping
   callbacks = [EarlyStopping(monitor='val_accuracy', patience=5)]
   model.fit(..., callbacks=callbacks)
   ```

## 📚 Resources

- TensorFlow Documentation: https://tensorflow.org/api_docs
- Keras Guide: https://keras.io/guides/
- CNN Basics: https://cs231n.github.io/convolutional-networks/
- Image Classification Best Practices: https://huggingface.co/docs/transformers/

## 🤝 Contributing

Feel free to improve this project:
- Add more data augmentation
- Implement transfer learning
- Add batch processing
- Improve UI/UX

## 📝 License

Free to use for educational and commercial purposes.

## ✨ Next Steps

1. ✅ Train model in notebook
2. ✅ Save trained model
3. ✅ Deploy with Streamlit/Flask
4. 🚀 Optional: Deploy to cloud
5. 📊 Optional: Monitor predictions
6. 🔄 Optional: Retrain with more data

## 🎓 Learning Outcomes

By completing this project, you'll understand:
- CNN architecture and how it works
- Image preprocessing and augmentation
- Model training and evaluation
- Metrics: accuracy, precision, recall, F1
- Web deployment of ML models
- Best practices for production ML

---

**Questions?** Check the notebook comments and function docstrings for detailed explanations.

Happy classifying! 🐱🐶

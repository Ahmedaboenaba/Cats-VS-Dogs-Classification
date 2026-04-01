# 🐱🐶 Cats vs Dogs Image Classifier

A beginner-friendly deep learning project that teaches you how to build, train, and deploy an AI model that can tell cats apart from dogs — just from a photo!

---

## 💡 What Does This Project Do?

You give it an image → it tells you: **"That's a Cat! 🐱"** or **"That's a Dog! 🐶"**, along with a confidence percentage.

The AI model was trained using a **Convolutional Neural Network (CNN)** — a type of neural network designed for image recognition.

---

## 📁 What's in This Repo?

Here's every file and what it does:

| File / Folder | What it does |
|---|---|
| `cats_Vs_Dogs CNN.ipynb` | **Main notebook** — train the AI model step by step |
| `app.py` | **Streamlit web app** — easiest way to use the model in a browser |
| `app_flask.py` | **Flask web app** — alternative web interface |
| `templates/index.html` | The HTML page displayed by the Flask app |
| `models/` | Folder containing the pre-trained model files (`.keras` and `.h5`) |
| `utils.py` | Helper functions to load the model and make predictions in Python |
| `config.py` | All settings in one place (image size, learning rate, paths, etc.) |
| `download_dataset.py` | Guide + helper to set up your image dataset folder |
| `requirements.txt` | All Python packages needed (full install) |
| `requirements-streamlit.txt` | Minimal packages for the Streamlit app only |
| `requirements-flask.txt` | Minimal packages for the Flask app only |
| `QUICKSTART.sh` | One-click setup script for **macOS / Linux** |
| `QUICKSTART.bat` | One-click setup script for **Windows** |
| `FILE_MANIFEST.md` | Detailed description of every file |
| `PROJECT_SUMMARY.md` | High-level project overview |

---

## 🚀 Quick Start (5 Steps)

### Step 1 — Install Python
Make sure you have **Python 3.8 or newer** installed.
Download from https://python.org if needed.

### Step 2 — Set Up the Project

**Windows** — double-click `QUICKSTART.bat`, or run in Command Prompt:
```bat
QUICKSTART.bat
```

**macOS / Linux** — run in Terminal:
```bash
bash QUICKSTART.sh
```

This will automatically:
- Create a virtual environment
- Install all required packages
- Create the `dataset/` folder structure

> 💡 **Prefer manual setup?** See the [Manual Setup](#manual-setup) section below.

### Step 3 — Add Your Images

Put your images inside the correct folders:
```
dataset/
├── cats/    ← put cat photos here (JPG or PNG)
└── dogs/    ← put dog photos here (JPG or PNG)
```

Aim for **at least 50–100 images per category** for decent accuracy.

**Free image sources:**
- [Pixabay](https://pixabay.com) — no account needed
- [Kaggle Cats & Dogs Dataset](https://www.kaggle.com/datasets) — search "cats and dogs"
- [Unsplash](https://unsplash.com)

> 💡 Run `python download_dataset.py` for a guided setup with download instructions.

### Step 4 — Train the Model

```bash
jupyter notebook
```

Open `cats_Vs_Dogs CNN.ipynb` and run all the cells from top to bottom.

The trained model will be saved automatically to the `models/` folder.

| Hardware | Time |
|---|---|
| CPU | ~10–15 minutes |
| GPU | ~2–5 minutes |

### Step 5 — Run the Web App

**Option A — Streamlit (recommended, easiest):**
```bash
streamlit run app.py
```
Open your browser at → http://localhost:8501

**Option B — Flask:**
```bash
python app_flask.py
```
Open your browser at → http://localhost:5000

Upload any cat or dog photo and the app will instantly tell you what it sees!

---

## 🧠 How to Use the Model in Python

You can also use the classifier directly in your own Python code:

```python
from utils import quick_predict

label, confidence = quick_predict('my_photo.jpg')
print(f"Result: {label} ({confidence:.1%} confidence)")
```

For batch predictions across a whole folder:
```python
from utils import batch_predict

results = batch_predict('./my_images/')
for r in results:
    print(f"{r['image']}: {r['prediction']} ({r['confidence']:.1%})")
```

---

## ⚙️ Configuration

All settings are in `config.py`. You can change things like:
- Image input size (default: 128×128)
- Number of training epochs (default: 10)
- Learning rate (default: 0.001)
- Batch size (default: 32)

```python
# config.py example settings
IMAGE_SIZE = (128, 128)
EPOCHS = 10
LEARNING_RATE = 0.001
BATCH_SIZE = 32
```

---

## 🤖 About the Model

The CNN model is built with TensorFlow/Keras and has this structure:

- **Input:** 128×128 pixel RGB image
- **3 Convolutional blocks** — detect edges, shapes, and features (32 → 64 → 128 filters)
- **MaxPooling layers** — reduce image size at each step
- **Dropout layers** — prevent overfitting (0.25 and 0.5)
- **Dense layers** — final decision layers (256 → 128 → 1 unit)
- **Output:** A number between 0 and 1 (below 0.5 = Cat, above 0.5 = Dog)

**Expected accuracy:** ~85%+ on the validation set

---

## ☁️ Deploy to the Cloud (Free)

Want to share your app online for free?

**Streamlit Cloud (easiest):**
1. Push your code to GitHub
2. Go to https://streamlit.io/cloud
3. Connect your repo and click **Deploy**

**Hugging Face Spaces:**
1. Create a free account at https://huggingface.co
2. Create a new Space → choose **Streamlit**
3. Upload `app.py`, `utils.py`, and your model file

**Google Colab (free GPU for training):**
1. Upload the notebook to https://colab.research.google.com
2. Enable GPU: Runtime → Change runtime type → GPU
3. Run all cells

---

## 🛠️ Manual Setup

If the quick start scripts didn't work, set up manually:

```bash
# 1. Create a virtual environment
python -m venv venv

# 2. Activate it
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Create dataset folders
mkdir -p dataset/cats dataset/dogs
```

---

## ❓ Troubleshooting

**"Model not found" error**
→ Train the model first by running all cells in `cats_Vs_Dogs CNN.ipynb`

**Low accuracy (below 70%)**
→ Add more images (aim for 200+ per category), or increase epochs in `config.py`

**Out of memory**
→ Reduce `BATCH_SIZE` or `IMAGE_SIZE` in `config.py`

**Streamlit won't start**
→ Run `pip install --upgrade streamlit`

**GPU not detected**
```bash
python -c "import tensorflow as tf; print(tf.config.list_physical_devices('GPU'))"
# If empty: pip install tensorflow[and-cuda]
```

---

## 📚 Learn More

- [TensorFlow Docs](https://tensorflow.org/api_docs)
- [Keras Guides](https://keras.io/guides/)
- [CNN Explained Simply](https://cs231n.github.io/convolutional-networks/)

---

## 📝 License

Free to use for learning and personal projects.

---

Happy classifying! 🐱🐶

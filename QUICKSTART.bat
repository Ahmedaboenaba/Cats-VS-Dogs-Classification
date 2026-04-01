@echo off
REM Quick Start Guide for Cats vs Dogs Classification (Windows)

cls
echo.
echo ==================================================
echo 🐱🐶 Cats vs Dogs - Quick Start Guide (Windows)
echo ==================================================
echo.

REM Check Python installation
echo ✓ Checking Python installation...
python --version
if errorlevel 1 (
    echo ❌ Python not found! Please install Python 3.8+ from https://python.org
    pause
    exit /b 1
)
echo.

REM Create virtual environment
echo 📦 Creating virtual environment...
python -m venv venv
echo.

REM Activate virtual environment
echo ✓ Activating virtual environment...
call venv\Scripts\activate.bat
echo.

REM Install dependencies
echo 📥 Installing dependencies (this may take 2-3 minutes)...
pip install -r requirements.txt -q
if errorlevel 1 (
    echo ❌ Installation failed!
    pause
    exit /b 1
)
echo ✓ Dependencies installed!
echo.

REM Create dataset directory
echo 📁 Creating dataset directory structure...
if not exist "dataset\cats" mkdir dataset\cats
if not exist "dataset\dogs" mkdir dataset\dogs
if not exist "models" mkdir models
echo ✓ Directory structure created
echo.

echo ==================================================
echo ✅ SETUP COMPLETE!
echo ==================================================
echo.
echo 📖 NEXT STEPS:
echo.
echo 1️⃣  PREPARE YOUR DATA:
echo    - Add cat images to: dataset\cats\
echo    - Add dog images to:  dataset\dogs\
echo    - Recommended: 100+ images per category
echo.
echo 2️⃣  TRAIN THE MODEL:
echo    jupyter notebook
echo    - Open 'cats_Vs_Dogs CNN.ipynb'
echo    - Run all cells (10-15 min on CPU, 2-5 min on GPU)
echo.
echo 3️⃣  DEPLOY THE APP:
echo.
echo    Option A (Recommended) - Streamlit:
echo    streamlit run app.py
echo    → Access at: http://localhost:8501
echo.
echo    Option B - Flask:
echo    python app_flask.py
echo    → Access at: http://localhost:5000
echo.
echo 4️⃣  DEPLOY TO CLOUD (Free Options):
echo    - Streamlit Cloud: https://streamlit.io/cloud
echo    - Hugging Face Spaces: https://huggingface.co/spaces
echo    - Google Colab: https://colab.research.google.com
echo.
echo ==================================================
echo.
pause

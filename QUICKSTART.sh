#!/bin/bash
# Quick Start Guide for Cats vs Dogs Classification

echo "=================================================="
echo "🐱🐶 Cats vs Dogs - Quick Start Guide"
echo "=================================================="
echo ""

# Check Python installation
echo "✓ Checking Python installation..."
python --version
echo ""

# Create virtual environment
echo "📦 Creating virtual environment..."
python -m venv venv
echo ""

# Activate virtual environment
echo "✓ Activating virtual environment..."
if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
    source venv/Scripts/activate
else
    source venv/bin/activate
fi
echo ""

# Install dependencies
echo "📥 Installing dependencies (this may take 2-3 minutes)..."
pip install -r requirements.txt -q
echo "✓ Dependencies installed!"
echo ""

# Create dataset directory
echo "📁 Creating dataset directory structure..."
mkdir -p dataset/cats
mkdir -p dataset/dogs
mkdir -p models
echo "✓ Directory structure created"
echo ""

echo "=================================================="
echo "✅ SETUP COMPLETE!"
echo "=================================================="
echo ""
echo "📖 NEXT STEPS:"
echo ""
echo "1️⃣  PREPARE YOUR DATA:"
echo "   - Add cat images to: dataset/cats/"
echo "   - Add dog images to:  dataset/dogs/"
echo "   - Recommended: 100+ images per category"
echo ""
echo "2️⃣  TRAIN THE MODEL:"
echo "   jupyter notebook"
echo "   - Open 'cats_Vs_Dogs CNN.ipynb'"
echo "   - Run all cells (10-15 min on CPU, 2-5 min on GPU)"
echo ""
echo "3️⃣  DEPLOY THE APP:"
echo ""
echo "   Option A (Recommended) - Streamlit:"
echo "   $ streamlit run app.py"
echo "   → Access at: http://localhost:8501"
echo ""
echo "   Option B - Flask:"
echo "   $ python app_flask.py"
echo "   → Access at: http://localhost:5000"
echo ""
echo "4️⃣  DEPLOY TO CLOUD (Free Options):"
echo "   - Streamlit Cloud: https://streamlit.io/cloud"
echo "   - Hugging Face Spaces: https://huggingface.co/spaces"
echo "   - Google Colab: https://colab.research.google.com"
echo ""
echo "=================================================="

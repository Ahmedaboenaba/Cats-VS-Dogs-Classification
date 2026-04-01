"""
Dataset Helper - Download sample cat and dog images

This script helps you quickly set up a dataset for training.
Uses Unsplash API to download free images.

Usage:
    python download_dataset.py

"""

import os
import requests
from pathlib import Path
from urllib.parse import urljoin
import time

def create_directories():
    """Create dataset directory structure"""
    dirs = ['dataset/cats', 'dataset/dogs']
    for dir_path in dirs:
        Path(dir_path).mkdir(parents=True, exist_ok=True)
        print(f"✓ Created: {dir_path}")

def download_from_unsplash(query, category, num_images=10):
    """
    Download images from Unsplash API

    Args:
        query: Search query (e.g., 'cat', 'dog')
        category: Folder to save to ('cats' or 'dogs')
        num_images: Number of images to download (default 10)
    """
    # Note: For production, use proper API key
    # Free API: 50 requests per hour without key

    print(f"\n📥 Downloading {num_images} {category} images from Unsplash...")
    print("   (This is a demonstration. For production use, register for API key)")
    print(f"   API URL: https://unsplash.com/api/")

    # Unsplash API endpoint
    api_url = "https://api.unsplash.com/search/photos"

    # Note: You'll need to get your own API key from:
    # https://unsplash.com/developers
    # Without key, you get limited requests

    params = {
        'query': query,
        'count': num_images,
        'orientation': 'landscape'
    }

    print("⚠️  To download images, you need an Unsplash API key:")
    print("   1. Go to: https://unsplash.com/developers")
    print("   2. Create an application")
    print("   3. Add your API key to this script")
    print("   4. Run again")

    return

def download_from_bing(query, category, num_images=10):
    """
    Alternative: Download from Bing Images
    Note: Always respect image copyright and terms of use
    """
    print(f"\n📥 Downloading {num_images} {category} images...")
    print("⚠️  Alternative: Use these services to download sample images:")
    print("   - Google Images: https://images.google.com")
    print("   - Pixabay: https://pixabay.com")
    print("   - Unsplash: https://unsplash.com")
    print("   - Pexels: https://pexels.com")
    print("   - Kaggle: https://kaggle.com/datasets")

def manual_download_guide():
    """Print guide for manual download"""
    print("\n" + "="*60)
    print("📖 MANUAL DOWNLOAD GUIDE")
    print("="*60)

    guide = """
1. PIXABAY (Recommended - Free, no registration needed)
   URL: https://pixabay.com
   Steps:
   a) Search for "cat" → Download high-res images to dataset/cats/
   b) Search for "dog" → Download high-res images to dataset/dogs/
   c) Download at least 50-100 images per category

2. UNSPLASH (Free, requires API key for automation)
   URL: https://unsplash.com
   Steps:
   a) Visit https://unsplash.com/developers
   b) Create application to get API key
   c) Use the key in this script

3. KAGGLE (Requires free account)
   URL: https://www.kaggle.com/datasets
   Search: "cats dogs dataset"
   Options:
   - "Cats and Dogs Images" by Aniket Chikane
   - "Cats and Dogs Dataset (2k breed images)"

4. COCO DATASET (Large, comprehensive)
   URL: https://cocodataset.org
   Steps:
   a) Download annotations
   b) Filter for cat/dog images
   c) Download images

5. MICROSOFT COCO
   URL: https://cocodataset.org/#download
   Download: 2017 Train/Val images

6. FLICKR-30K (30,000 images)
   URL: https://github.com/BryanPlummer/flickr30k_entities
   Steps:
   a) Request dataset access
   b) Download and filter for cats/dogs

MINIMUM DATASET:
- At least 20-30 images per category to start
- Aim for 50-100+ for better accuracy
- 200+ per category for production

QUALITY TIPS:
✓ Diverse poses and lighting
✓ Various backgrounds
✓ Different breeds/types
✗ Avoid duplicate images
✗ Avoid cartoon/drawings
✗ Avoid heavily edited photos
"""

    print(guide)

def create_sample_structure():
    """Create the directory structure"""
    print("\n" + "="*60)
    print("🗂️  SETTING UP DIRECTORY STRUCTURE")
    print("="*60)

    create_directories()

    print("\n✅ Directory structure ready!")
    print("\nYour structure:")
    print("""
    dataset/
    ├── cats/
    │   ├── cat1.jpg
    │   ├── cat2.jpg
    │   └── ...
    └── dogs/
        ├── dog1.jpg
        ├── dog2.jpg
        └── ...
    """)

def main():
    print("\n" + "="*60)
    print("🐱🐶 DATASET HELPER - Cats vs Dogs Classification")
    print("="*60)

    # Create directory structure
    create_sample_structure()

    # Show download options
    manual_download_guide()

    print("\n" + "="*60)
    print("⏭️  NEXT STEPS")
    print("="*60)
    print("""
1. Download images from Pixabay/Unsplash/Kaggle
2. Organize them in dataset/cats/ and dataset/dogs/
3. Run: jupyter notebook
4. Open: cats_Vs_Dogs CNN.ipynb
5. Train the model (2-3 minutes)
6. Deploy with Streamlit!

Happy training! 🚀
    """)

if __name__ == '__main__':
    main()

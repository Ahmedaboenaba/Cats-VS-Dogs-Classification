# Cats vs. Dogs Image Classification 🐱🐶

This repository contains a Jupyter Notebook demonstrating an end-to-end deep learning pipeline to classify images as either a cat or a dog. It utilizes a Transfer Learning with MobileNetV2 built with TensorFlow and Keras to extract visual features and make binary predictions.

## Features

* **Data Handling & Preprocessing:** Loads and prepares the image data, standardizing image dimensions and scaling pixel values to optimize model training.
* **Data Augmentation:** Implements techniques (like rotation, zooming, and flipping) to artificially expand the training dataset, making the model more robust and preventing overfitting.
* **Transfer Learning with MobileNetV2:** Constructs a custom neural network using sequential `Conv2D` and `MaxPooling2D` layers to capture spatial hierarchies in the images, followed by fully connected `Dense` layers for the final binary classification.
* **Model Training & Callbacks:** Trains the model using binary crossentropy loss and optimizes it using standard callbacks (such as `EarlyStopping` or learning rate reduction) to achieve the best convergence.
* **Performance Evaluation:** Visualizes training and validation metrics (accuracy and loss) across epochs to track learning progress and identify potential overfitting.
* **Inference:** Evaluates the model on unseen test images and outputs the predicted class (Cat or Dog).

## Prerequisites

To run this notebook on your local machine, you will need Python installed along with the following primary libraries:

* `tensorflow` (includes `keras`)
* `numpy`
* `matplotlib`

You can install the required dependencies using pip:


## Dataset

This project assumes the use of a standard binary image dataset, such as the widely used Kaggle Cats and Dogs dataset. If running locally, ensure your dataset is downloaded and properly structured into `train` and `validation` directories before executing the notebook.
Dataset link: https://www.kaggle.com/datasets/bhavikjikadara/dog-and-cat-classification-dataset

## Usage

1. Clone this repository to your local machine.
2. Open the `Cats_VS_Dogs_classification.ipynb` file using Jupyter Notebook, JupyterLab, or upload it to Google Colab.
3. Ensure the dataset paths in the notebook correctly point to your local image directories.
4. Run the cells sequentially to preprocess the data, build the CNN, train the model, and evaluate its performance.

## Results

*(Note: Update this section with your specific model results)*

* **Validation Accuracy:** 0.9678
* **Validation Loss:** 0.0763
* The model successfully distinguishes between cats and dogs with high confidence on the test set.

---

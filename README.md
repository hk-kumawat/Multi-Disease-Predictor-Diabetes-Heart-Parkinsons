# Multi Disease Predictor 🏥
<div style="text-align: center;">
    <img src="https://github.com/user-attachments/assets/c42649e8-9826-4d6e-a7e9-75fdf7c4bfa3" alt="Multi Disease Predictor" width="450"/> 
</div>

## Overview

The Multi Disease Predictor is a machine learning project that predicts the likelihood of three diseases: diabetes, heart disease, and Parkinson's disease. Using various health indicators, this project implements machine learning algorithms to provide accurate predictions, enhancing early detection and preventive healthcare.

## Live Demo

Explore the Multi Disease Predictor! 👉🏻 [![Experience It! 🌟](https://img.shields.io/badge/Experience%20It!-blue)](https://multidiseasepredictor.streamlit.app/)

<br>

- _Below is a preview of the Multi Disease Predictor in action. Input your health parameters to receive predictions. Check out the user-friendly interface and accurate results!_ 👇🏻

![Screenshot 2024-10-31 021313](https://github.com/user-attachments/assets/60949976-d8af-4b9a-a871-43ff961758de)

## Table of Contents

1. [Features](#features)
2. [Datasets](#datasets)
3. [Data Preprocessing](#data-preprocessing)
4. [Model Training](#model-training)
5. [Evaluation](#evaluation)
6. [Installation](#installation)
7. [Usage](#usage)
8. [Technologies Used](#technologies-used)
9. [Results](#results)
10. [Conclusion](#conclusion)
11. [Contact](#contact)

<br>

## Features🌟

- Predicts the likelihood of diabetes, heart disease, and Parkinson's disease.
- Loads and preprocesses datasets for each disease.
- Utilizes machine learning models for accurate predictions.
- Saves trained models for future predictions.

<br>

## Datasets📊

- **Diabetes Dataset**: [Diabetes.csv](https://www.kaggle.com/datasets/saurabh00007/diabetescsv)
- **Heart Disease Dataset**: [Heart.csv](https://www.kaggle.com/datasets/arezaei81/heartcsv)
- **Parkinson's Disease Dataset**: [Parkinsons.csv](https://www.kaggle.com/datasets/gargmanas/parkinsonsdataset)

Each dataset includes relevant health features for the prediction tasks.

<br>

## Data Preprocessing🛠

1. **Data Cleaning**: Non-numeric columns are dropped to focus on relevant numeric predictors.
2. **Feature Scaling**: Applied normalization or standardization for consistency across models.

<br>

## Model Training🧠

- The models used in this project include:
  - **Diabetes Prediction**: Implemented with Support Vector Machine (SVM).
  - **Heart Disease Prediction**: Utilizes Logistic Regression.
  - **Parkinson's Disease Prediction**: Also implemented with SVM.
  
- Each model is trained and evaluated through the following `.ipynb` scripts:
  - **Diabetes Prediction**: `diabetes_model.ipynb`
  - **Heart Disease Prediction**: `heart_disease_model.ipynb`
  - **Parkinson's Disease Prediction**: `parkinsons_model.ipynb`
  
- After training, the trained models are saved as:
  - `diabetes_model.sav`
  - `heart_disease_model.sav`
  - `parkinsons_model.sav`

<br>

## Evaluation📈

Each model is evaluated using:
- **Accuracy Score**: Measures how often the classifier is correct.
- **Confusion Matrix**: Visual representation of the model's performance.
- **Classification Report**: Provides precision, recall, and F1 score for each class.

<br>

## Installation🛠

1. **Clone the repository**:
   ```bash
   git clone https://github.com/hk-kumawat/multi-disease-predictor.git
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

<br>

## Usage🚀

1. **Train the models**: Run the three `.ipynb` files to train and save the models.
2. **Model Inference**:
   - Load the trained models in `app.py` using the following files:
     - `diabetes_model.sav`
     - `heart_disease_model.sav`
     - `parkinsons_model.sav`
   - Input your health parameters in the deployed Streamlit application to receive predictions.

<br>

## Technologies Used💻

- Python
- Libraries: `pandas`, `numpy`, `scikit-learn`, `pickle`
- Deployment: Streamlit for user interface

<br>

## Results🏆

In the **Results** section, you could include some sample output images that demonstrate how the Multi Disease Predictor works for each disease type. Here's a suggested description:

---

## Results 🏆

Below are some sample outputs of the **Multi Disease Predictor** for each of the three diseases: diabetes, heart disease, and Parkinson's. These images illustrate the application's interface, showcasing user inputs and the resulting predictions for different health indicators. The output is straightforward, providing users with a clear understanding of their predicted health status.

### Sample Output Images

1. **Diabetes Prediction**  
   - **Description**: This example demonstrates a user's input values for diabetes-related health indicators, with the resulting prediction displayed as either "Diabetes Detected" or "No Diabetes Detected."

2. **Heart Disease Prediction**  
   - **Description**: Here, the input values relate to risk factors associated with heart disease, with the application outputting either "Heart Disease Detected" or "No Heart Disease Detected."

3. **Parkinson's Disease Prediction**  
   - **Description**: This output shows the application's prediction for Parkinson's disease, where specific health metrics are analyzed, leading to a result of either "Parkinson's Disease Detected" or "No Parkinson's Disease Detected."


<br>

## Conclusion📚

The Multi Disease Predictor project demonstrates the application of machine learning in healthcare for predicting diseases based on health parameters. The models are trained and evaluated, highlighting the importance of data preprocessing and model selection. Deploying the models on Streamlit allows users easy access to health predictions.

<br>

## Contact

### 📬 Get in Touch!
I’d love to hear from you! Feel free to reach out:

- [![GitHub](https://img.shields.io/badge/GitHub-hk--kumawat-blue?logo=github)](https://github.com/hk-kumawat) 💻 — Explore my projects and contributions.
- [![LinkedIn](https://img.shields.io/badge/LinkedIn-Harshal%20Kumawat-blue?logo=linkedin)](https://www.linkedin.com/in/harshal-kumawat/) 🌐 — Let’s connect professionally.
- [![Email](https://img.shields.io/badge/Email-harshalkumawat100@gmail.com-blue?logo=gmail)](mailto:harshalkumawat100@gmail.com) 📧 — Send me an email for any in-depth discussions.

---

Feel free to customize any parts further, especially the links and images, to fit your project!

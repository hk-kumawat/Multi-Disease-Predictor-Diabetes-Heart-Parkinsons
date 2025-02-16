<a id="readme-top"></a>

# Multi Disease Predictor 🏥
<div style="text-align: center;">
    <img src="https://github.com/user-attachments/assets/c42649e8-9826-4d6e-a7e9-75fdf7c4bfa3" alt="Multi Disease Predictor" width="450"/> 
</div>

## Overview

The **Multi Disease Predictor** is an interactive web application built using **Streamlit** that leverages machine learning to predict three common health conditions: **Diabetes**, **Heart Disease**, and **Parkinson's Disease**. Users can input relevant clinical parameters through an intuitive interface, and the app returns real-time predictions using pre-trained models stored as pickle files. This project demonstrates how to integrate multiple models into one cohesive tool for early disease detection.


<br>


## Live Demo

Explore the Multi Disease Predictor! 👉🏻 [![Experience It! 🌟](https://img.shields.io/badge/Experience%20It!-blue)](https://multidiseasepredictor.streamlit.app/)

<br>

_Below is a preview of the Multi Disease Predictor in action. Enter medical parameters to get instant health insights! 👇_

![Screenshot 2024-10-31 021313](https://github.com/user-attachments/assets/60949976-d8af-4b9a-a871-43ff961758de)

<br>


## Learning Journey 🗺️

Developing the Multi Disease Predictor was a transformative experience that broadened my skills in both machine learning and interactive app development, here's the story behind it:

- **Inspiration:**  
  The intersection of healthcare and AI has always fascinated me. I wanted to create a tool that could assist in early disease detection while making complex medical predictions more accessible.

- **Why I Made It:**  
  I aimed to develop a system that could:
  - Help in early disease detection
  - Make medical screening more accessible
  - Demonstrate the practical application of ML in healthcare
  - Serve as an educational tool for understanding health parameters

- **Challenges Faced:**  
  - **Model Selection:** Finding the right algorithms for each disease prediction
  - **Data Preprocessing:** Handling medical data with appropriate scaling and normalization
  - **Feature Selection:** Identifying the most relevant medical parameters
  - **User Interface:** Creating an intuitive interface for medical parameters
  - **Ethical Considerations:** Implementing appropriate disclaimers and user guidance

- **What I Learned:**  
  - **Data Analysis:** Medical data preprocessing and validation
  - **Model Evaluation:** Comparing different ML algorithms for medical applications
  - **UI/UX Design:** Creating user-friendly medical interfaces

This project has solidified my understanding of deploying machine learning models in real-world applications and highlighted the importance of accessible healthcare tools.

<br>


## Table of Contents

1. [Features](#features)
2. [Installation](#installation)    
3. [Usage](#usage)    
4. [Technologies Used](#technologies-used)   
5. [Datasets](#datasets)
6. [Data Preprocessing](#data-preprocessing)
7. [Model Training](#model-training)
8. [Results](#results)
9. [Model Preformance](#model-performance)
10. [Directory Structure](#directory-structure)
11. [Contributing](#contributing)
12. [License](#license)
13. [Contact](#contact)
14. [Future Enhancements](#future-enhancements)

<br>

## Features🌟

- **Multiple Predictions:**  
  - Predicts Diabetes, Heart Disease, and Parkinson's Disease using specialized models.
- **Interactive Interface:**  
  - A user-friendly Streamlit app with input forms for each condition.
- **Real-Time Feedback:**  
  - Immediate predictions and clear diagnostic messages.
- **Comprehensive Data Handling:**  
  - Processes and validates clinical input to ensure accurate predictions.
- **Modular Design:**  
  - Easily navigate between different disease prediction modules using a sidebar menu.
    
- **Comprehensive Health Parameters:**
  - Diabetes: 8 parameters
  - Heart Disease: 13 parameters
  - Parkinson's: 22 parameters


<br>


## Installation🛠

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/hk-kumawat/Multi-Disease-Predictor.git
   cd hk-kumawat-multi-disease-predictor
   ```

2. **Create & Activate a Virtual Environment (Optional but Recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate      # On Windows: venv\Scripts\activate
   ```

3. **Install Required Packages:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application:**
   ```bash
   streamlit run app.py
   ```

5. **(Optional) Use Dev Container:**
   - Open the project in an IDE that supports Dev Containers using `.devcontainer/devcontainer.json`.

<br>



## Usage🚀

1. **Launch the Streamlit app:**
```bash
streamlit run app.py
```

2. **Select Disease Type:**
   - Choose from the sidebar menu
   - Enter relevant medical parameters
   - Click "Predict" for results

3. **Explore Different Predictions:**
   - Diabetes Prediction
   - Heart Disease Prediction
   - Parkinson's Disease Prediction

### Jupyter Notebooks
Explore the model development process:
```bash
jupyter notebook "diabetes.ipynb"
jupyter notebook "heart.ipynb"
jupyter notebook "parkinsons.ipynb"
```

<br>

## Technologies Used💻

- **Programming Language:**  
  - Python

- **Machine Learning:**  
  - scikit-learn (Logistic Regression, SVM, KNN, Naive Bayes)

- **Web Framework:**  
  - Streamlit

- **Data Handling & Visualization:**  
  - Pandas, NumPy, Matplotlib, Seaborn

- **Model Persistence:**  
  - pickle

- **Additional Libraries:**  
  - streamlit_option_menu

<br>


## Datasets📊

- **Diabetes Dataset**: [Diabetes.csv](https://www.kaggle.com/datasets/saurabh00007/diabetescsv)
- **Heart Disease Dataset**: [Heart.csv](https://www.kaggle.com/datasets/arezaei81/heartcsv)
- **Parkinson's Disease Dataset**: [Parkinsons.csv](https://www.kaggle.com/datasets/gargmanas/parkinsonsdataset)

Each dataset includes relevant health features for the prediction tasks.

<br>


## Data Preprocessing🔄

- **Data Loading:**  
  - Load datasets using Pandas and review with `.head()`, `.describe()`, and `.info()`.

- **Data Cleaning:**  
  - Check for and handle missing values and duplicates.

- **Feature Separation:**  
  - Separate input features from target variables.

- **Train-Test Split:**  
  - Split the data with stratification using `train_test_split`.

- **Encoding & Scaling:**  
  - Encode categorical targets and scale features as needed.

This streamlined process ensures clean, reliable data for accurate model predictions.

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



## Results🏆

Below are some sample outputs of the **Multi Disease Predictor** for each of the three diseases: diabetes, heart disease, and Parkinson's. These images illustrate the application's interface, showcasing user inputs and the resulting predictions for different health indicators. The output is straightforward, providing users with a clear understanding of their predicted health status.

<br>

### 1.  **Diabetes Prediction:**  
   This example demonstrates a user's input values for diabetes-related health indicators, with the resulting prediction displayed as either "Diabetes Detected" or "No Diabetes Detected.<br>

![Screenshot 2024-10-31 025040](https://github.com/user-attachments/assets/a3da41bf-bda1-4bfb-829d-6a609a1a8080)

<br>

### 2. **Heart Disease Prediction:**  
   Here, the input values relate to risk factors associated with heart disease, with the application outputting either "Heart Disease Detected" or "No Heart Disease Detected. <br>

![heart](https://github.com/user-attachments/assets/65d19811-d491-4cbf-8d93-5357c0e742af)

<br>

### 3. **Parkinson's Disease Prediction:**  
   This output shows the application's prediction for Parkinson's disease, where specific health metrics are analyzed, leading to a result of either "Parkinson's Disease Detected" or "No Parkinson's Disease Detected.
<br>

![parkinsons](https://github.com/user-attachments/assets/074fda68-0329-45b1-8e6b-c1dc279f96f0)


<br>


## Model Performance🏆

### Accuracy Scores:
- **Diabetes Model:** 78.7%
- **Heart Disease Model:** 85.2%
- **Parkinson's Model:** 87.2%

### System Metrics:
- **Average Prediction Time:** <1s
- **Model Size:** Combined 15KB
- **Reliability:** Cross-validated predictions
- **Interface:** Responsive and user-friendly

<br>


## Directory Structure📁

```plaintext
multi-disease-predictor/
├── README.md                    # Project documentation
├── app.py                       # Streamlit application
├── requirements.txt             # Dependencies
├── saved_models/               # Trained model files
│   ├── diabetes_model.sav      # Diabetes prediction model
│   ├── heart_disease_model.sav # Heart disease model
│   └── parkinsons_model.sav    # Parkinson's model
├── notebooks/                  # Model development notebooks
│   ├── diabetes.ipynb          # Diabetes model notebook
│   ├── heart.ipynb            # Heart disease model notebook
│   └── parkinsons.ipynb       # Parkinson's model notebook
└── datasets/                   # Input datasets
    ├── diabetes.csv           # Diabetes dataset
    ├── heart.csv             # Heart disease dataset
    └── parkinsons.csv        # Parkinson's dataset
```

<br> 


## Future Enhancements🚀

- **Expanded Disease Coverage:**  
  - Integrate additional disease prediction modules to cover more health conditions.
    
- **Improved Model Accuracy:**  
  - Incorporate advanced algorithms and hyperparameter tuning for even better predictions.
    
- **User Interface Enhancements:**  
  - Add dynamic visualizations, charts, and more intuitive navigation.
    
- **Mobile Compatibility:**  
  - Develop a mobile-responsive version of the app.
    
- **Real-Time Data Updates:**  
  - Enable live updates and integration with external health data sources.
    
- **User Feedback Integration:**  
  - Add a feedback system to continuously improve the model based on user inputs.
 
<br>

  

## Contributing🤝
Contributions make the open source community such an amazing place to learn, inspire, and create. 🙌 Any contributions you make are greatly appreciated! 😊

Have an idea to improve this project? Go ahead and fork the repo to create a pull request, or open an issue with the tag **"enhancement"**. Don't forget to give the project a star! ⭐ Thanks again! 🙏

<br>

1. **Fork** the repository.

2. **Create** a new branch:
   ```bash
   git checkout -b feature/YourFeatureName
   ```

3. **Commit** your changes with a descriptive message.

4. **Push** to your branch:
   ```bash
   git push origin feature/YourFeatureName
   ```

5. **Open** a Pull Request detailing your enhancements or bug fixes.

<br> 


## License📝

This project is licensed under the **MIT License** - see the [LICENSE](./LICENSE) file for details.

<br>

## Contact

### 📬 Get in Touch!
I’d love to hear from you! Feel free to reach out:

- [![GitHub](https://img.shields.io/badge/GitHub-hk--kumawat-blue?logo=github)](https://github.com/hk-kumawat) 💻 — Explore my projects and contributions.
- [![LinkedIn](https://img.shields.io/badge/LinkedIn-Harshal%20Kumawat-blue?logo=linkedin)](https://www.linkedin.com/in/harshal-kumawat/) 🌐 — Let’s connect professionally.
- [![Email](https://img.shields.io/badge/Email-harshalkumawat100@gmail.com-blue?logo=gmail)](mailto:harshalkumawat100@gmail.com) 📧 — Send me an email for any in-depth discussions.

<br>



## Thanks for exploring—stay healthy! 🏥

> "Prevention is better than cure." – Desiderius Erasmus

<p align="right">(<a href="#readme-top">back to top</a>)</p>

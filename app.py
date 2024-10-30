import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Set page configuration
st.set_page_config(page_title="Health Assistant", layout="wide", page_icon="🧑‍⚕️")

# getting the working directory of the main.py
working_dir = os.path.dirname(os.path.abspath(__file__))

# loading the saved models
diabetes_model = pickle.load(open(f'{working_dir}/saved_models/diabetes_model.sav', 'rb'))
heart_disease_model = pickle.load(open(f'{working_dir}/saved_models/heart_disease_model.sav', 'rb'))
parkinsons_model = pickle.load(open(f'{working_dir}/saved_models/parkinsons_model.sav', 'rb'))

# sidebar for navigation
with st.sidebar:
    selected = option_menu(
        'Multi Disease Predictor',
        ['Diabetes Prediction', 'Heart Disease Prediction', 'Parkinsons Prediction'],
        menu_icon='🩺',
        icons=['activity', 'heart', 'person'],
        default_index=0
    )
    st.markdown('<div class="sidebar-footer">Developed by - Harshal Kumawat with 💚</div>', unsafe_allow_html=True)

# Display disclaimer with custom styling
st.markdown("""
<div style="
    background-color: #ffffff;
    padding: 15px;
    border-radius: 5px;
    border: 1px solid #ccc;
    color: #333;
    font-size: 0.9em;
">  <h5 style='color: #333;'>Disclaimer:</h5>
    The predictions provided by this tool are based on a machine learning model trained on a limited dataset and should be interpreted with caution. While this app aims to support awareness and early indications, it is not a substitute for professional medical testing. For accurate and reliable diagnoses, please consult a healthcare provider and consider lab-based tests. Rely on this tool as an educational aid, not as definitive medical advice.
</div>
""", unsafe_allow_html=True)
    
# Diabetes Prediction Page
if selected == 'Diabetes Prediction':
    st.title('🩸Diabetes Prediction')

    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.number_input(
            '👶 Number of Pregnancies', help="Enter the total number of pregnancies."
        )
    with col2:
        Glucose = st.number_input(
            '🍬 Glucose Level (mg/dL)', help="Enter the glucose level in mg/dL."
        )
    with col3:
        BloodPressure = st.number_input(
            '💉 Blood Pressure (mm Hg)', help="Enter the blood pressure in mm Hg."
        )
    with col1:
        SkinThickness = st.number_input(
            '📏 Skin Thickness (mm)', help="Enter the skin fold thickness in mm."
        )
    with col2:
        Insulin = st.number_input(
            '💉 Insulin Level (IU/mL)', help="Enter the insulin level in IU/mL."
        )
    with col3:
        BMI = st.number_input(
            '⚖️ BMI (kg/m²)', help="Enter the Body Mass Index (BMI) in kg/m²."
        )
    with col1:
        DiabetesPedigreeFunction = st.number_input(
            '📈 Diabetes Pedigree Function', help="Enter the diabetes pedigree function value."
        )
    with col2:
        Age = st.number_input(
            '🎂 Age (years)', help="Enter the age of the person in years."
        )

    if st.button('🩺Predict Diabetes'):
        user_input = [float(x) for x in [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]]
        diab_prediction = diabetes_model.predict([user_input])
        diab_diagnosis = '⚠️ Alert! You are diabetic' if diab_prediction[0] == 1 else '🎉 Great news! Your results indicate that you are not diabetic! Keep up the healthy lifestyle!😄'
        st.success(diab_diagnosis)

# Heart Disease Prediction Page
if selected == 'Heart Disease Prediction':
    st.title('🫀Heart Disease Prediction')

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.number_input('🎂 Age', help="Enter the person's age in years.")
    with col2:
        sex = st.number_input('👤 Sex (0: Female, 1: Male)', help="Enter 0 for female and 1 for male.")
    with col3:
        cp = st.number_input('💔 Chest Pain Type (0-3)', help="Enter the type of chest pain (0-3).")
    with col1:
        trestbps = st.number_input('💉 Resting Blood Pressure (mm Hg)', help="Enter the resting blood pressure in mm Hg.")
    with col2:
        chol = st.number_input('🧪 Serum Cholesterol (mg/dL)', help="Enter serum cholesterol in mg/dL.")
    with col3:
        fbs = st.number_input('🍬 Fasting Blood Sugar > 120 mg/dL (0/1)', help="Enter 1 if fasting blood sugar > 120 mg/dL, else enter 0.")
    with col1:
        restecg = st.number_input('📊 Resting ECG Results (0-2)', help="Enter ECG results (0-2).")
    with col2:
        thalach = st.number_input('💓 Max Heart Rate Achieved', help="Enter the maximum heart rate achieved.")
    with col3:
        exang = st.number_input('🏃 Exercise Induced Angina (0/1)', help="Enter 1 if exercise-induced angina is present, else enter 0.")
    with col1:
        oldpeak = st.number_input('📉 ST Depression', help="Enter the ST depression induced by exercise.")
    with col2:
        slope = st.number_input('⛰️ Slope of Peak Exercise ST Segment (0-2)', help="Enter the slope of the peak exercise ST segment (0-2).")
    with col3:
        ca = st.number_input('🩺 Number of Major Vessels (0-3)', help="Enter the number of major vessels colored by fluoroscopy (0-3).")
    with col1:
        thal = st.number_input('🧬 Thalassemia Type (0-2)', help="Enter thalassemia type (0: Normal, 1: Fixed Defect, 2: Reversible Defect).")

    if st.button('🩺Predict Heart Disease'):
        user_input = [float(x) for x in [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]]
        heart_prediction = heart_disease_model.predict([user_input])
        heart_diagnosis = '💔 Alert! You have heart disease. It is time to take action and prioritize your heart health! 🫀' if heart_prediction[0] == 1 else '🎉 Awesome! Your results show a healthy heart! Keep it beating strong with a balanced diet and regular exercise! 💖'
        st.success(heart_diagnosis)

# Parkinson's Prediction Page
if selected == "Parkinsons Prediction":
    st.title("🧠Parkinson's Disease Prediction")

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        fo = st.number_input('🔊 MDVP:Fo(Hz)', help="Enter average vocal fundamental frequency in Hz.")
    with col2:
        fhi = st.number_input('🔊 MDVP:Fhi(Hz)', help="Enter maximum vocal fundamental frequency in Hz.")
    with col3:
        flo = st.number_input('🔊 MDVP:Flo(Hz)', help="Enter minimum vocal fundamental frequency in Hz.")
    with col4:
        Jitter_percent = st.number_input('📈 MDVP:Jitter(%)', help="Enter jitter percentage.")
    with col5:
        Jitter_Abs = st.number_input('📈 MDVP:Jitter(Abs)', help="Enter absolute jitter.")
    with col1:
        RAP = st.number_input('📉 MDVP:RAP', help="Enter relative amplitude perturbation.")
    with col2:
        PPQ = st.number_input('📉 MDVP:PPQ', help="Enter five-point period perturbation quotient.")
    with col3:
        DDP = st.number_input('📉 Jitter:DDP', help="Enter the degree of jitter.")
    with col4:
        Shimmer = st.number_input('✨ MDVP:Shimmer', help="Enter shimmer.")
    with col5:
        Shimmer_dB = st.number_input('✨ MDVP:Shimmer(dB)', help="Enter shimmer in dB.")
    with col1:
        APQ3 = st.number_input('🔔 Shimmer:APQ3', help="Enter three-point amplitude perturbation quotient.")
    with col2:
        APQ5 = st.number_input('🔔 Shimmer:APQ5', help="Enter five-point amplitude perturbation quotient.")
    with col3:
        APQ = st.number_input('🔔 MDVP:APQ', help="Enter amplitude perturbation quotient.")
    with col4:
        DDA = st.number_input('📊 Shimmer:DDA', help="Enter the degree of amplitude perturbation.")
    with col5:
        NHR = st.number_input('📊 NHR', help="Enter the noise-to-harmonics ratio.")
    with col1:
        HNR = st.number_input('🎤 HNR', help="Enter harmonics-to-noise ratio.")
    with col2:
        RPDE = st.number_input('🔎 RPDE', help="Enter recurrence period density entropy.")
    with col3:
        DFA = st.number_input('📐 DFA', help="Enter detrended fluctuation analysis.")
    with col4:
        spread1 = st.number_input('📏 Spread1', help="Enter spread1 value.")
    with col5:
        spread2 = st.number_input('📏 Spread2', help="Enter spread2 value.")
    with col1:
        D2 = st.number_input('🧬 D2', help="Enter D2 value.")
    with col2:
        PPE = st.number_input('🔍 PPE', help="Enter pitch period entropy.")

    if st.button("🩺Predict Parkinson's"):
        user_input = [float(x) for x in [fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP, Shimmer, Shimmer_dB, APQ3, APQ5, APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]]
        parkinsons_prediction = parkinsons_model.predict([user_input])
        parkinsons_diagnosis = "⚠️ Important! You've been diagnosed with Parkinson's disease! But remember, you have the strength to face this challenge! 💪" if parkinsons_prediction[0] == 1 else "🎉 Great news! Your results indicate no signs of Parkinson's! Keep moving and thriving! 🚴‍♀️"
        st.success(parkinsons_diagnosis)




import os
import joblib
import pandas as pd
import numpy as np
from tensorflow import keras
from sklearn.ensemble import RandomForestClassifier

# === Path Absolut berbasis lokasi file ini ===
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def abspath(filename):
    return os.path.join(BASE_DIR, filename)

# === Load Encoder & Scaler ===
le_gender     = joblib.load(abspath('encoder_gender.joblib'))
le_occupation = joblib.load(abspath('encoder_occupation.joblib'))
le_bmi        = joblib.load(abspath('encoder_bmi.joblib'))
le_disorder   = joblib.load(abspath('encoder_disorder.joblib'))

scaler_quality  = joblib.load(abspath('scaler_quality.joblib'))
scaler_duration = joblib.load(abspath('scaler_duration.joblib'))
scaler_disorder = joblib.load(abspath('scaler_disorder.joblib'))

# === Load Model Regresi (TF) & Random Forest (RF) ===
model_quality  = keras.models.load_model(abspath('model_quality.keras'))
model_duration = keras.models.load_model(abspath('model_duration.keras'))
model_disorder = joblib.load(abspath('model_disorder.joblib'))  # <--- MODEL 3: RF!

# === List fitur sesuai pipeline training ===
features_quality = [
    'Gender_cod', 'Age', 'Occupation_cod',
    'Physical Activity Level', 'Stress Level',
    'BMI Category_cod', 'Heart Rate', 'Daily Steps'
]
features_duration = features_quality + ['Pred_Quality']
features_disorder = features_duration + ['Pred_Duration']

# === Occupation Grouping (minoritas jadi "Lainnya") ===
MINORITY_OCCS = ['Sales Representative', 'Manager', 'Scientist', 'Software Engineer']
def clean_occupation(occ):
    occ_title = occ.strip().title()
    if occ_title in MINORITY_OCCS:
        return 'Others'
    return occ_title

# === Clipping fitur numerik pada input user ===
def clip_user_input(user):
    user = user.copy()
    user['Heart Rate']   = min(max(int(user['Heart Rate']), 62), 80)
    user['Daily Steps']  = min(max(int(user['Daily Steps']), 2000), 11600)
    # Tambah fitur lain jika perlu
    return user

# === Encoding user input ===
def encode_user(user_dict):
    user = user_dict.copy()
    user['Gender_cod']        = le_gender.transform([user['Gender'].strip().capitalize()])[0]
    user['Occupation_cod']    = le_occupation.transform([user['Occupation']])[0]
    user['BMI Category_cod']  = le_bmi.transform([user['BMI Category'].strip().title()])[0]
    return user

# === PIPELINE PREDICT ===
def pipeline_predict(user_input):
    # 1. Clipping dan cleaning
    user = clip_user_input(user_input)
    user['Occupation'] = clean_occupation(user['Occupation'])
    # 2. Encoding
    user_enc = encode_user(user)

    # 3. Predict Quality of Sleep (Regresi, TF)
    X_q = pd.DataFrame([user_enc])[features_quality]
    X_q_scaled = scaler_quality.transform(X_q)
    pred_quality = float(model_quality.predict(X_q_scaled)[0][0])
    user_enc['Pred_Quality'] = pred_quality

    # 4. Predict Sleep Duration (Regresi, TF)
    X_d = pd.DataFrame([user_enc])[features_duration]
    X_d_scaled = scaler_duration.transform(X_d)
    pred_duration = float(model_duration.predict(X_d_scaled)[0][0])
    user_enc['Pred_Duration'] = pred_duration

    # 5. Predict Sleep Disorder (Klasifikasi, RandomForest)
    X_c = pd.DataFrame([user_enc])[features_disorder]
    X_c_scaled = scaler_disorder.transform(X_c)
    pred_disorder_code = int(model_disorder.predict(X_c_scaled)[0])
    pred_disorder_probs = model_disorder.predict_proba(X_c_scaled)[0]
    pred_disorder_label = le_disorder.inverse_transform([pred_disorder_code])[0]

    return {
        "quality_of_sleep": round(pred_quality, 2),
        "sleep_duration": round(pred_duration, 2),
        "sleep_disorder": pred_disorder_label,
        "disorder_probs": {label: float(pred_disorder_probs[i]) for i, label in enumerate(le_disorder.classes_)}
    }

# === Optional: Uji sample input ===
if __name__ == "__main__":
    sample_input = {
        'Gender': 'Male',
        'Age': 25,
        'Occupation': 'Scientist',  # Akan jadi "Lainnya"
        'Physical Activity Level': 3,
        'Stress Level': 4,
        'BMI Category': 'Overweight',
        'Heart Rate': 80,          # Akan di-clip ke 78
        'Daily Steps': 15000       # Akan di-clip ke 10000
    }
    result = pipeline_predict(sample_input)
    print(result)

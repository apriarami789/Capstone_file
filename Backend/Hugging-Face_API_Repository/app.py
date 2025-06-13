from fastapi import FastAPI
from pydantic import BaseModel
from model_handler import pipeline_predict

app = FastAPI(
    title="Sleep Health Predictor API",
    description="Prediksi Quality of Sleep, Sleep Duration, dan Sleep Disorder via FastAPI. © 2024 Sleep Health Capstone Demo",
    version="2.0.0"
)

class PredictRequest(BaseModel):
    Gender: str
    Age: int
    Occupation: str
    Physical_Activity_Level: int
    Stress_Level: int
    BMI_Category: str
    Heart_Rate: int
    Daily_Steps: int

@app.post("/predict")
def predict(req: PredictRequest):
    user_input = {
        "Gender": req.Gender,
        "Age": req.Age,
        "Occupation": req.Occupation,
        "Physical Activity Level": req.Physical_Activity_Level,
        "Stress Level": req.Stress_Level,
        "BMI Category": req.BMI_Category,
        "Heart Rate": req.Heart_Rate,
        "Daily Steps": req.Daily_Steps
    }
    result = pipeline_predict(user_input)
    return {
        "quality_of_sleep": float(result["quality_of_sleep"]),
        "sleep_duration": float(result["sleep_duration"]),
        "sleep_disorder": result["sleep_disorder"],
        "disorder_probs": result["disorder_probs"]
    }

@app.get("/")
def root():
    return {
        "message": "Welcome to Sleep Health Predictor API! Use the /predict endpoint to POST your data and get predictions."
    }

# Tambah Health Endpoint untuk Monitoring
@app.get("/health")
def health():
    return {"status": "ok", "message": "API and models are healthy"}

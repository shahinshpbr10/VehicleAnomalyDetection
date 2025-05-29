from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

# Load the trained model
model = joblib.load("model.pkl")

# Create the FastAPI app
app = FastAPI(title="Vehicle Anomaly Detector")

# Define the input schema
class VehicleInput(BaseModel):
    engine_temp: float
    rpm: int

# Define the prediction endpoint
@app.post("/predict")
def predict(data: VehicleInput):
    features = np.array([[data.engine_temp, data.rpm]])
    prediction = model.predict(features)[0]
    return {
        "engine_temp": data.engine_temp,
        "rpm": data.rpm,
        "anomaly": bool(prediction),
        "status": "High Temp " if prediction == 1 else "Normal "
    }

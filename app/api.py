from fastapi import FastAPI
import joblib
import pandas as pd

model = joblib.load("models/fraud_xgb.joblib")
# scaler = joblib.load("models/scaler.joblib")  # Uncomment if you used a scaler

app = FastAPI()

@app.post("/predict")
def predict(input_data: dict):
    df = pd.DataFrame([input_data])
    # df = scaler.transform(df)  # Uncomment if you used a scaler
    proba = model.predict_proba(df)[:, 1][0]
    label = int(proba > 0.5)
    return {"fraud_probability": float(proba), "fraud_prediction": label}

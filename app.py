from fastapi import FastAPI
import joblib
import pandas as pd

app = FastAPI()

model = joblib.load("models/model.joblib")
model_columns = joblib.load("models/columns.joblib")

@app.post("/predict")
def predict(data: dict):
    df = pd.DataFrame([data])

    for col in model_columns:
        if col not in df.columns:
            df[col] = 0

    df = df[model_columns]

    prediction = model.predict(df)[0]
    return {"predicted_delivery_time": float(prediction)}
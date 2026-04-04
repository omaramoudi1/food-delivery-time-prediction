from enum import Enum
from pathlib import Path
import logging
from typing import Annotated

import joblib
import pandas as pd
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field, ConfigDict, StrictFloat, StrictInt


# Logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


# Enums for categorical inputs
class WeatherEnum(str, Enum):
    Clear = "Clear"
    Rainy = "Rainy"
    Foggy = "Foggy"
    Windy = "Windy"
    Snowy = "Snowy"


class TrafficLevelEnum(str, Enum):
    Low = "Low"
    Medium = "Medium"
    High = "High"


class TimeOfDayEnum(str, Enum):
    Morning = "Morning"
    Afternoon = "Afternoon"
    Evening = "Evening"
    Night = "Night"


class VehicleTypeEnum(str, Enum):
    Bike = "Bike"
    Scooter = "Scooter"
    Car = "Car"



# Request schema

class PredictionInput(BaseModel):
    model_config = ConfigDict(extra="forbid")

    Distance_km: Annotated[StrictFloat, Field(gt=0)]
    Weather: WeatherEnum
    Traffic_Level: TrafficLevelEnum
    Time_of_Day: TimeOfDayEnum
    Vehicle_Type: VehicleTypeEnum
    Preparation_Time_min: Annotated[StrictInt, Field(ge=0)]
    Courier_Experience_yrs: Annotated[StrictFloat, Field(ge=0)]


# Paths
BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "models" / "model_pipeline.joblib"


# App
app = FastAPI(
    title="Delivery Time Prediction API",
    description="API for predicting delivery time in minutes.",
    version="1.0.0"
)

model = None


# Startup
@app.on_event("startup")
def load_model() -> None:
    global model
    try:
        if not MODEL_PATH.exists():
            raise FileNotFoundError(f"Model file not found: {MODEL_PATH}")

        model = joblib.load(MODEL_PATH)
        logger.info("Model loaded successfully from %s", MODEL_PATH)

    except Exception as e:
        logger.exception("Failed to load model")
        raise RuntimeError(f"Could not load model: {e}") from e


# Routes
@app.get("/")
def root() -> dict[str, str]:
    return {"message": "Delivery Time Prediction API is running."}


@app.get("/health")
def health() -> dict[str, str]:
    if model is None:
        raise HTTPException(status_code=503, detail="Model is not loaded")
    return {"status": "ok"}


@app.post("/predict")
def predict(data: PredictionInput) -> dict[str, float]:
    if model is None:
        raise HTTPException(status_code=503, detail="Model is not loaded")

    try:
        input_dict = data.model_dump()
        df = pd.DataFrame([input_dict])

        prediction = model.predict(df)[0]

        logger.info("Prediction request: %s", input_dict)
        logger.info("Prediction response: %s", prediction)

        return {"predicted_delivery_time": float(prediction)}

    except Exception as e:
        logger.exception("Prediction failed")
        raise HTTPException(
            status_code=400,
            detail=f"Prediction failed: {str(e)}"
        ) from e
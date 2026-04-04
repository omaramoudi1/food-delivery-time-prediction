# Food Delivery Time Prediction

## Project Overview
This project aims to predict the **delivery time of food orders** using Machine Learning techniques.  
Accurate delivery time estimation helps improve customer satisfaction and optimize logistics.

---

## Objective
Build a model that predicts delivery time based on:
- Distance  
- Preparation time  
- Traffic conditions  
- Weather conditions  
- Time of day  
- Courier experience  
- Vehicle type  

---

## Dataset Description
Features:

- `Distance_km` → Delivery distance  
- `Preparation_Time_min` → Order preparation time  
- `Courier_Experience_yrs` → Courier experience  
- `Weather` → Weather condition  
- `Traffic_Level` → Traffic intensity  
- `Time_of_Day` → Time period  
- `Vehicle_Type` → Type of vehicle  

**Target:**
- `Delivery_Time_min` → Delivery time (minutes)

---

## Machine Learning Pipeline

### 1. Preprocessing
- Handle missing values  
- Encode categorical variables using Pipeline + OneHotEncoder  
- Remove irrelevant columns  

### 2. Models
- Linear Regression  
- Random Forest  
- Gradient Boosting  

### 3. Evaluation
- MAE  
- RMSE  
- R²  
- Cross-validation  

---

## Results
Linear Regression achieved the best performance on this dataset.

---

## API (FastAPI)

## Example Input

A sample request is provided in `sample.json` to test the API quickly.

You can use it with curl:

```bash
curl -X POST http://127.0.0.1:8000/predict \
-H "Content-Type: application/json" \
-d @sample.json
```

### Run
uvicorn app:app --reload

### Swagger
http://127.0.0.1:8000/docs

### Example Request
{
  "Distance_km": 5.2,
  "Weather": "Rainy",
  "Traffic_Level": "Medium",
  "Time_of_Day": "Evening",
  "Vehicle_Type": "Scooter",
  "Preparation_Time_min": 18,
  "Courier_Experience_yrs": 2
}

### Example Response
{
  "predicted_delivery_time": 45.91
}

---

## Validation
- Strict types  
- Enum for categorical values  
- Invalid inputs rejected  

---

## Project Structure
delivery_project/
├── data/
├── models/
│   └── model_pipeline.joblib
├── notebook.ipynb
├── app.py
├── requirements.txt
└── README.md

---

## Installation
git clone <repo_url>  
cd delivery_project  
pip install -r requirements.txt  

---

## Future Improvements
- Add real-time data  
- Try advanced models  
- Deploy on cloud  

---

## Author
Omar Amoudi  
3rd year Computer Science Student

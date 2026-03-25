# Food Delivery Time Prediction

## Project Overview
This project aims to predict the **delivery time of food orders** using Machine Learning techniques.  
Accurate delivery time estimation is crucial for improving customer satisfaction and optimizing logistics in food delivery services.

---

## Objective
The goal is to build a predictive model that estimates delivery time based on several factors such as:
- Distance between restaurant and customer  
- Preparation time  
- Traffic conditions  
- Weather conditions  
- Time of the day  
- Courier experience  
- Vehicle type  

---

## Dataset Description
The dataset contains information about delivery orders with the following features:

- `Distance_km` → Distance of delivery  
- `Preparation_Time_min` → Time to prepare the order  
- `Courier_Experience_yrs` → Experience of the delivery person  
- `Weather_*` → Weather conditions (Foggy, Rainy, Snowy, Windy)  
- `Traffic_Level_*` → Traffic intensity (Low, Medium)  
- `Time_of_Day_*` → Time period (Morning, Evening, Night)  
- `Vehicle_Type_*` → Type of vehicle (Car, Scooter)  

**Target variable:**
- `Delivery_Time_min` → Delivery time (in minutes)

---

## Machine Learning Pipeline

### 1. Data Preprocessing
- Handling missing values  
- Encoding categorical variables using one-hot encoding  
- Removing irrelevant features (e.g. `Order_ID`)  

### 2. Models Used
- Linear Regression  
- Random Forest Regressor  
- Gradient Boosting Regressor  

### 3. Evaluation Metric
- **Mean Absolute Error (MAE)**  
 Chosen because it is directly interpretable in minutes

---

## Results
The **Random Forest model** achieved the best performance, capturing non-linear relationships between features and delivery time.

Example prediction:
```json
{
  "predicted_delivery_time": 45.91
}
```

---

## API Deployment (FastAPI)

The trained model is deployed using **FastAPI**, allowing real-time predictions.

###  Run the API
```bash
python -m uvicorn app:app --reload
```

### Access Swagger UI
http://127.0.0.1:8000/docs

### Example Request
```json
{
  "Distance_km": 5.2,
  "Preparation_Time_min": 18,
  "Courier_Experience_yrs": 2,
  "Weather_Foggy": 0,
  "Weather_Rainy": 1,
  "Weather_Snowy": 0,
  "Weather_Windy": 0,
  "Traffic_Level_Low": 0,
  "Traffic_Level_Medium": 1,
  "Time_of_Day_Evening": 1,
  "Time_of_Day_Morning": 0,
  "Time_of_Day_Night": 0,
  "Vehicle_Type_Car": 0,
  "Vehicle_Type_Scooter": 1
}
```

---

## Project Structure
```
delivery_project/
│
├── data/
├── models/
├── outputs/
├── notebook.ipynb
├── train.py
├── app.py
├── requirements.txt
└── README.md
```

---

## Installation

### 1. Clone the repository
```bash
git clone <repo_url>
cd delivery_project
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

---

## Future Improvements
- Use real-time traffic data  
- Integrate GPS coordinates  
- Add deep learning models  
- Deploy on cloud (AWS, GCP)  
- Build a web interface (Streamlit)

---

## Key Takeaways
- Machine learning can significantly improve delivery time estimation  
- Feature engineering plays a crucial role  
- Tree-based models perform well on structured data  
- FastAPI enables easy deployment of ML models  

---

## Author
Omar Amoudi  
3rd year Computer Science Student  

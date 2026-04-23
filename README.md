# 🏠 EstimaAI — House Price Prediction System

A full-stack web application that predicts California house prices using a trained **Random Forest pipeline**.

---

## 📁 Project Structure

```bash
your-folder/
├── app.py                  # Flask backend (API server)
├── index.html              # Frontend UI
├── requirements.txt        # Python dependencies
├── rf_pipeline_model.pkl   # Trained model (NOT included in repo)
└── README.md
```

---

## 🚀 Setup & Run

### 1️⃣ Place the model

Copy `rf_pipeline_model.pkl` into the same folder as `app.py`.

> ⚠️ Note: Model file is not included in this repo due to GitHub size limits.

---

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

### 3️⃣ Start Flask server

```bash
python app.py
```

You should see:

```text
✅ Model loaded successfully from rf_pipeline_model.pkl
🏠 House Price Prediction API
========================================
Model path : rf_pipeline_model.pkl
Model ready: True
Server     : http://localhost:5000
========================================
```

---

### 4️⃣ Open the UI

* Open `index.html` manually
  **OR**
* Visit: http://127.0.0.1:5000/

---

## 🔌 API Endpoints

### ▶️ POST `/predict`

#### Request

```json
{
  "MedInc": 8.3252,
  "HouseAge": 41.0,
  "AveRooms": 6.984127,
  "AveBedrms": 1.023810,
  "Population": 322.0,
  "AveOccup": 2.555556,
  "Latitude": 37.88,
  "Longitude": -122.23
}
```

#### Response

```json
{
  "prediction": 4.265793,
  "price_dollars": 426579.30,
  "price_formatted": "$426,579"
}
```

---

### ▶️ GET `/health`

Check if the server and model are running correctly.

---

## 📊 Input Features

| Feature    | Description                 | Example |
| ---------- | --------------------------- | ------- |
| MedInc     | Median income (in $10,000s) | 8.3252  |
| HouseAge   | Median house age            | 41      |
| AveRooms   | Avg rooms per household     | 6.98    |
| AveBedrms  | Avg bedrooms per household  | 1.02    |
| Population | Block population            | 322     |
| AveOccup   | Avg household members       | 2.55    |
| Latitude   | Location latitude           | 37.88   |
| Longitude  | Location longitude          | -122.23 |

---

## 💡 Output

Model output is multiplied by **100,000** to get the price in USD.

Example:

```text
4.265793 → $426,579
```

---

## 🛠️ Tech Stack

* Python
* Flask
* Scikit-learn
* Joblib
* HTML / CSS / JavaScript

---

## 👤 Author

Ayush Mittal

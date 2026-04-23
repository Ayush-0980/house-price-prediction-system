# 🏠 EstimaAI — House Price Prediction System

A full-stack web application that predicts California house prices using a trained
Random Forest pipeline (`rf_pipeline_model.pkl`).

---

## 📁 Project Structure

```
your-folder/
├── app.py                  ← Flask backend (API server)
├── index.html              ← Frontend UI
├── requirements.txt        ← Python dependencies
├── rf_pipeline_model.pkl   ← Your trained model  ⬅ place here
└── README.md
```

---

## 🚀 Setup & Run

### 1. Place your model
Copy `rf_pipeline_model.pkl` into the same folder as `app.py`.

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Start the Flask server
```bash
python app.py
```
You should see:
```
✅ Model loaded successfully from rf_pipeline_model.pkl
🏠 House Price Prediction API
========================================
  Model path : rf_pipeline_model.pkl
  Model ready: True
  Server     : http://localhost:5000
========================================
```

### 4. Open the UI
Open `index.html` in your browser, **or** navigate to:
```
http://localhost:5000
```

---

## 🔌 API Endpoints

### `POST /predict`
Send a JSON body with all 8 features:
```json
{
  "MedInc":     8.3252,
  "HouseAge":   41.0,
  "AveRooms":   6.984127,
  "AveBedrms":  1.023810,
  "Population": 322.0,
  "AveOccup":   2.555556,
  "Latitude":   37.88,
  "Longitude":  -122.23
}
```

**Response:**
```json
{
  "prediction":      4.265793,
  "price_dollars":   426579.30,
  "price_formatted": "$426,579",
  "input": { ... }
}
```

### `GET /health`
Check if the server and model are running correctly.

---

## 📊 Input Features

| Feature     | Description                          | Example  |
|-------------|--------------------------------------|----------|
| MedInc      | Median income (in $10,000s)          | 8.3252   |
| HouseAge    | Median house age in block group      | 41       |
| AveRooms    | Average rooms per household          | 6.984127 |
| AveBedrms   | Average bedrooms per household       | 1.02381  |
| Population  | Block group population               | 322      |
| AveOccup    | Average number of household members  | 2.555556 |
| Latitude    | Block group latitude                 | 37.88    |
| Longitude   | Block group longitude                | -122.23  |

**Output** is multiplied by 100,000 to get the price in USD.
(e.g., model output `4.265793` → `$426,579`)

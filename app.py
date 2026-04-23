from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import joblib
import numpy as np
import pandas as pd
import os

app = Flask(__name__, static_folder=".")
CORS(app)

# Load the trained pipeline model
MODEL_PATH = "rf_pipeline_model.pkl"

try:
    model = joblib.load(MODEL_PATH)
    print(f"✅ Model loaded successfully from {MODEL_PATH}")
except FileNotFoundError:
    print(f"❌ Model file not found at {MODEL_PATH}. Place rf_pipeline_model.pkl in the same directory.")
    model = None

FEATURE_COLUMNS = [
    "MedInc",
    "HouseAge",
    "AveRooms",
    "AveBedrms",
    "Population",
    "AveOccup",
    "Latitude",
    "Longitude",
]


@app.route("/")
def index():
    return send_from_directory(".", "index.html")


@app.route("/predict", methods=["POST"])
def predict():
    if model is None:
        return jsonify({"error": "Model not loaded. Please check the server logs."}), 500

    try:
        data = request.get_json()

        # Validate and extract features
        features = {}
        for col in FEATURE_COLUMNS:
            if col not in data:
                return jsonify({"error": f"Missing field: {col}"}), 400
            try:
                features[col] = float(data[col])
            except (ValueError, TypeError):
                return jsonify({"error": f"Invalid value for {col}: must be a number"}), 400

        # Build DataFrame with correct column order
        input_df = pd.DataFrame([features], columns=FEATURE_COLUMNS)

        # Predict
        prediction = model.predict(input_df)
        price = float(prediction[0])

        # California Housing dataset prices are in $100,000 units
        price_dollars = price * 100_000

        return jsonify({
            "prediction": round(price, 6),
            "price_dollars": round(price_dollars, 2),
            "price_formatted": f"${price_dollars:,.0f}",
            "input": features,
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/health")
def health():
    return jsonify({
        "status": "ok",
        "model_loaded": model is not None,
        "model_path": MODEL_PATH,
    })


if __name__ == "__main__":
    print("\n🏠 House Price Prediction API")
    print("=" * 40)
    print(f"  Model path : {MODEL_PATH}")
    print(f"  Model ready: {model is not None}")
    print("  Server     : http://localhost:5000")
    print("=" * 40 + "\n")
    app.run(debug=True, host="0.0.0.0", port=5000)

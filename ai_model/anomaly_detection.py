import numpy as np
from sklearn.ensemble import IsolationForest
import joblib
import logging
import os
from config import Config

def train_model(data):
    try:
        model = IsolationForest(n_estimators=100, contamination=0.1)
        model.fit(data)
        joblib.dump(model, Config.MODEL_PATH)
        logging.info("Anomaly detection model trained and saved.")
    except Exception as e:
        logging.error(f"Error training model: {e}")

def detect_anomalies(new_data):
    try:
        if not os.path.exists(Config.MODEL_PATH):
            logging.error(f"Model not found at {Config.MODEL_PATH}")
            return []
        model = joblib.load(Config.MODEL_PATH)
        predictions = model.predict(new_data)
        anomalies = new_data[predictions == -1]
        return anomalies
    except Exception as e:
        logging.error(f"Error detecting anomalies: {e}")
        return []

if __name__ == "__main__":
    # Example test
    test_data = np.random.rand(10, 10)
    train_model(test_data)
    anomalies = detect_anomalies(test_data)
    print(f"Detected anomalies: {anomalies}")

import numpy as np
import logging

def preprocess_log_data(log_data):
    try:
        # Example preprocessing: converting logs into numeric features
        # Assuming log_data is a list of log dictionaries
        processed_data = []
        for log in log_data:
            # Convert each log's features to numerical data
            features = [hash(log[key]) % 1000 for key in log.keys()]
            processed_data.append(features)
        
        return np.array(processed_data)
    except Exception as e:
        logging.error(f"Error in data preprocessing: {e}")
        return np.array([])

if __name__ == "__main__":
    # Example log data
    log_data = [{"source_ip": "192.168.1.1", "event": "login", "severity": "high"}]
    processed_data = preprocess_log_data(log_data)
    print(f"Processed data: {processed_data}")

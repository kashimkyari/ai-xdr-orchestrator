import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    KAFKA_TOPIC = os.getenv('KAFKA_TOPIC', 'security_logs')
    KAFKA_BOOTSTRAP_SERVERS = os.getenv('KAFKA_BOOTSTRAP_SERVERS', 'localhost:9092')
    GROUP_ID = os.getenv('GROUP_ID', 'incident_detector')
    MODEL_PATH = os.getenv('MODEL_PATH', 'models/anomaly_detection_model.pkl')
    DECISION_MODEL_PATH = os.getenv('DECISION_MODEL_PATH', 'models/decision_model.pkl')

if __name__ == "__main__":
    # For testing purposes
    print(f"KAFKA_TOPIC: {Config.KAFKA_TOPIC}")
    print(f"KAFKA_BOOTSTRAP_SERVERS: {Config.KAFKA_BOOTSTRAP_SERVERS}")

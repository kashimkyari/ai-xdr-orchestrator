import random
import joblib
import logging
from config import Config

ACTIONS = ['quarantine', 'block_ip', 'isolate_network', 'notify_team']

def train_decision_model():
    try:
        joblib.dump(ACTIONS, Config.DECISION_MODEL_PATH)
        logging.info("Decision model saved.")
    except Exception as e:
        logging.error(f"Error training decision model: {e}")

def decide_action(anomaly_score):
    try:
        if not os.path.exists(Config.DECISION_MODEL_PATH):
            logging.error(f"Decision model not found at {Config.DECISION_MODEL_PATH}")
            return 'no_action'
        model = joblib.load(Config.DECISION_MODEL_PATH)
        return random.choice(model) if anomaly_score > 0.8 else 'no_action'
    except Exception as e:
        logging.error(f"Error in decision making: {e}")
        return 'no_action'

if __name__ == "__main__":
    # Example usage
    anomaly_score = random.random()
    action = decide_action(anomaly_score)
    print(f"Decided action: {action}")

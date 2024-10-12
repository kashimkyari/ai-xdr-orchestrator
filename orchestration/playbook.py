import logging
from ai_model.decision_making import decide_action

def run_playbook(anomalies, execute_action_callback):
    try:
        for anomaly in anomalies:
            anomaly_score = random.random()  # Replace with real scoring logic
            action = decide_action(anomaly_score)
            execute_action_callback(action)
    except Exception as e:
        logging.error(f"Error in playbook: {e}")

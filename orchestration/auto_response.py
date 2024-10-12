import logging
from orchestration.playbook import run_playbook
from ai_model.anomaly_detection import detect_anomalies

def automated_response(log_data, execute_action_callback):
    try:
        anomalies = detect_anomalies(log_data)
        run_playbook(anomalies, execute_action_callback)
    except Exception as e:
        logging.error(f"Error in automated response: {e}")

from flask import Flask, request, jsonify
import logging
from orchestration.auto_response import automated_response
from data_ingestion.data_preprocessing import preprocess_log_data

app = Flask(__name__)

@app.route('/trigger', methods=['POST'])
def trigger_incident_response():
    try:
        log_data = request.json.get('log_data', [])
        if log_data:
            processed_data = preprocess_log_data(log_data)
            automated_response(processed_data, execute_action)
            return jsonify({"status": "response triggered"}), 200
        else:
            return jsonify({"error": "no log data provided"}), 400
    except Exception as e:
        logging.error(f"Error in API trigger: {e}")
        return jsonify({"error": "internal server error"}), 500

def execute_action(action):
    logging.info(f"Executing action: {action}")

if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0', port=5000)

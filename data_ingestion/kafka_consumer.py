import json
import logging
from kafka import KafkaConsumer
from data_ingestion.data_preprocessing import preprocess_log_data
from orchestration.auto_response import automated_response
from config import Config

logging.basicConfig(level=logging.INFO)

consumer = KafkaConsumer(
    Config.KAFKA_TOPIC,
    bootstrap_servers=Config.KAFKA_BOOTSTRAP_SERVERS.split(','),
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id=Config.GROUP_ID,
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

def consume_logs():
    try:
        for message in consumer:
            log_data = message.value
            logging.info(f"Received log: {log_data}")
            processed_data = preprocess_log_data([log_data])
            automated_response(processed_data, execute_action)
    except Exception as e:
        logging.error(f"Error consuming logs: {e}")

def execute_action(action):
    logging.info(f"Executing action: {action}")

if __name__ == "__main__":
    consume_logs()

import base64
import json

def process_log_entry(event, context):
    """
    Triggered by a message on a Pub/Sub topic.
    This function decodes and prints the log message.
    """

    # The log message is in the 'data' filed, encoded in Base64
    log_data_encoded = event['data']
    log_data_encoded_str = base64.b64decode(log_data_encoded).decode('utf-8')

    # Convert the string log data into python dictionray.
    log_payload = json.loads(log_data_encoded_str)

    print("--- New log received by Cloud Function ---")
    print(f"Log Text: {log_payload.get('textPayload')}")
    print(f"Timestamp: {log_payload.get('timestamp')}")
    print(f"Severity: {log_payload.get('severity')}")
    print("-------------------------------------------")
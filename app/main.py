import requests
import json
import time

LOGSTASH_URL = "http://logstash:5000"

def send_log(event):
    headers = {"Content-Type": "application/json"}
    response = requests.post(LOGSTASH_URL, data=json.dumps(event), headers=headers)
    print(f"Sent log: {event} - Response: {response.status_code}")

if __name__ == "__main__":
    while True:
        event = {
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
            "event_type": "unauthorized_access",
            "message": "Intento de acceso no autorizado detectado",
            "severity": "high"
        }
        send_log(event)
        time.sleep(10)  # Enviar logs cada 10 segundos
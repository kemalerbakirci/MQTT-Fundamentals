import time
import json
import threading
from app.mqtt_client import create_client
import os

#Loads publishing topic (default: sensors/temperature).
TOPIC_PUB = os.getenv('TOPIC_PUB', 'sensors/temperature')


#Creates MQTT client for publishing.
def publish_sensor_data(interval: float = 2.0):
    client = create_client(client_id="publisher")
    client.loop_start()

    #Infinite loop sending JSON messages every interval seconds.
    try:
        while True:
            payload = {
                "timestamp": time.time(),
                "value": round(20 + 10 * os.urandom(1)[0] / 255, 2)  # random 20–30°C
            }
            client.publish(TOPIC_PUB, json.dumps(payload))
            print(f"[PUBLISH] {payload}")
            time.sleep(interval)

    #Handles Ctrl+C safely and disconnects cleanly.        
    except KeyboardInterrupt:
        pass
    finally:
        client.loop_stop()
        client.disconnect()

import threading
import json
import os
from app.mqtt_client import create_client

TOPIC_SUB = os.getenv('TOPIC_SUB', 'sensors/temperature')

#Callback when a new message arrives.
def on_message(client, userdata, msg):
    data = json.loads(msg.payload.decode())
    print(f"[MESSAGE] {data}")

#Creates client, subscribes to TOPIC_SUB.
def start_subscriber():
    client = create_client(client_id="subscriber")
    client.on_message = on_message
    client.subscribe(TOPIC_SUB)
    client.loop_forever()

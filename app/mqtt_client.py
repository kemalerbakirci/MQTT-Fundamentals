import os
import logging
from dotenv import load_dotenv
import paho.mqtt.client as mqtt

#Finds the .env file inside config/.
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '..', 'config', 'settings.env'))

#Reads broker URL and port.
BROKER_URL = os.getenv('BROKER_URL')
BROKER_PORT = int(os.getenv('BROKER_PORT', '1883'))

#Configures logging.
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


#Creates a client with client_id (unique per publisher/subscriber).
def create_client(client_id: str) -> mqtt.Client:
    """Instantiate and connect an MQTT client."""
    client = mqtt.Client(client_id=client_id)
    client.on_connect = on_connect
    client.on_disconnect = on_disconnect
    client.connect(BROKER_URL, BROKER_PORT)
    return client


#Logs connection result. rc == 0 → success.
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        logger.info("Connected to MQTT broker")
    else:
        logger.error(f"Connection failed with code {rc}")


#Logs when client disconnects.
def on_disconnect(client, userdata, rc):
    logger.info("Disconnected from MQTT broker (rc=%s)", rc)

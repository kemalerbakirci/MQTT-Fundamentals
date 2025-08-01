import sys
from app.publisher import publish_sensor_data
from app.subscriber import start_subscriber
import threading

MENU = """
MQTT Pub/Sub Dashboard
1) Start publishing sensor data
2) View received messages
3) Exit
Choose an option: """

def main():
    while True:
        choice = input(MENU).strip()
        if choice == '1':
            threading.Thread(target=publish_sensor_data, daemon=True).start()
            print("Publishing sensor data... Press Ctrl+C to stop.")
        elif choice == '2':
            threading.Thread(target=start_subscriber, daemon=True).start()
            print("Subscribed. Press Ctrl+C to exit subscriber.")
        elif choice == '3':
            print("Goodbye!")
            sys.exit(0)
        else:
            print("Invalid option, try again.")

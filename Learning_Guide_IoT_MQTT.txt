# MQTT Fundamentals – Learning Guide

## 📌 Overview
This project introduces the basics of MQTT (Message Queuing Telemetry Transport) using a simple CLI-based publisher-subscriber system.  
It is designed to help beginners understand how MQTT works in real IoT scenarios.

---

## 1️⃣ What is MQTT?
MQTT is a lightweight messaging protocol for IoT devices.  
It uses a **publish/subscribe model**:
- **Broker**: The central server that receives and distributes messages.
- **Publisher**: A device or script that sends messages to the broker.
- **Subscriber**: A device or script that listens to messages from the broker.

---

## 2️⃣ Project Goal
- Learn how to create a **publisher** that sends sensor data.
- Learn how to create a **subscriber** that receives and displays data.
- Understand **topics** and how publishers and subscribers communicate.

---

## 3️⃣ Key Concepts
### ✅ Topics
A **topic** is like a channel where messages are sent.  
Example: `home/sensors/temperature`.

### ✅ QoS
- **QoS 0**: At most once (no confirmation, fastest).
- **QoS 1**: At least once (message is delivered but may be duplicated).
- **QoS 2**: Exactly once (ensures no duplication).

---

## 4️⃣ What You Learn from This Project
✅ How to use the `paho-mqtt` library.  
✅ How to connect to a public MQTT broker (like `test.mosquitto.org`).  
✅ How to publish and subscribe to messages.  
✅ How to use a CLI menu to interact with MQTT operations.

---

## 5️⃣ Recommended Learning Steps
1. Understand basic Python (functions, loops, imports).
2. Learn JSON basics (`json.dumps()`, `json.loads()`).
3. Install Mosquitto locally (`brew install mosquitto` on macOS).
4. Try publishing and subscribing to topics.
5. Modify the project to add more sensors or new topics.

---

## 📚 Resources
- MQTT Essentials: https://www.hivemq.com/mqtt-essentials/
- Paho MQTT Python Docs: https://pypi.org/project/paho-mqtt/


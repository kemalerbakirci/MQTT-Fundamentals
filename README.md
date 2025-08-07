# MQTT Pub/Sub Dashboard (CLI-based)

## 📌 Overview
This project is a **CLI-based dashboard** that combines **MQTT Publisher and Subscriber** into a single application.  
It demonstrates **IoT fundamentals**, **MQTT communication**, and **asynchronous operations** in Python.

The project is designed with a **modular, professional structure** to be pushed directly to GitHub and serve as part of a portfolio.

If you want to have basic information about the subject: Learning_Guide_IoT_MQTT.md

---

## 📂 Directory Structure
```
mqtt_dashboard/
├── app/
│   ├── __init__.py
│   ├── mqtt_client.py      # Handles MQTT connection setup
│   ├── publisher.py        # Publishes simulated sensor data
│   ├── subscriber.py       # Receives messages from broker
│   └── cli.py              # CLI dashboard for user interaction
│
├── config/
│   └── settings.env        # Environment variables (broker URL, topics)
│
├── requirements.txt        # Project dependencies
├── README.md               # Project documentation
└── run.py                  # Application entry point
```

---

## ⚙️ Features
✅ Simulated **temperature sensor data** publishing  
✅ MQTT **subscription to live messages**  
✅ CLI **menu for easy interaction**  
✅ Uses **environment variables** for broker settings  
✅ Clean **logging** and **graceful shutdown**  
✅ Modular structure ready for GitHub portfolio  

---

## 📦 Requirements
- Python 3.8+
- Virtual environment (recommended)

---

## 🚀 Setup Instructions

### 1️⃣ Clone Repository
```bash
git clone <repo-url>
cd mqtt_dashboard
```

### 2️⃣ Create Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate   # macOS/Linux
# OR
venv\Scripts\activate    # Windows
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

---

## ⚙️ Configure Environment Variables
Edit `config/settings.env`:
```
BROKER_URL=test.mosquitto.org
BROKER_PORT=1883
TOPIC_PUB=sensors/temperature
TOPIC_SUB=sensors/temperature
```

---

## ▶️ How to Run
Run the CLI application:
```bash
python run.py
```

### CLI Menu:
```
MQTT Pub/Sub Dashboard
1) Start publishing sensor data
2) View received messages
3) Exit
Choose an option:
```

- **Option 1** → Starts publishing random sensor data to the broker.  
- **Option 2** → Subscribes to the topic and prints messages live.  
- **Option 3** → Exits the application.  

---

## 🛠 How It Works
- **Publisher** sends JSON messages (timestamp, value) to the broker at regular intervals.  
- **Subscriber** listens to the same topic and prints messages in real time.  
- Both run **asynchronously** using Python threads.  

---

## 📜 Logging
Logs connection and disconnection events automatically:
```
INFO:app.mqtt_client:Connected to MQTT broker
INFO:app.mqtt_client:Disconnected from MQTT broker (rc=0)
```

---

## 🤝 Contributing
- Fork the repository
- Create a feature branch
- Commit changes with meaningful messages
- Open a pull request

---

## 📄 License
This project is open-source under the MIT License.

---

## 🎯 Learning Objectives
- Understand **MQTT Pub/Sub communication**
- Practice **environment variable management**
- Use **logging and modular project structure**
- Build a **GitHub-ready IoT simulation project**

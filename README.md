# 🚀 MQTT Fundamentals - IoT Communication Project

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![MQTT](https://img.shields.io/badge/MQTT-Protocol-green.svg)](https://mqtt.org)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## 📌 Overview

A **professional CLI-based MQTT dashboard** that demonstrates IoT fundamentals through publisher-subscriber communication patterns. This project combines **MQTT Publisher and Subscriber** functionality into a single, interactive application.

**Perfect for learning:**
- IoT communication protocols
- MQTT pub/sub patterns
- Asynchronous Python programming
- Professional project structure

> 📚 **New to MQTT?** Check out our comprehensive [Learning Guide](docs/Learning_Guide_IoT_MQTT.md) to get started!

---

## 🏗️ Project Structure

```
MQTT-Fundamentals/
├── 📁 app/                    # Core application modules
│   ├── __init__.py           # Package initialization
│   ├── mqtt_client.py        # MQTT connection & configuration
│   ├── publisher.py          # Sensor data publisher
│   ├── subscriber.py         # Message subscriber & handler
│   └── cli.py                # Interactive CLI dashboard
├──  docs/                  # Documentation files
│   ├── Learning_Guide_IoT_MQTT.md  # MQTT learning guide
│   └── CONTRIBUTING.md       # Contribution guidelines
├── 📄 requirements.txt       # Python dependencies
├── 📄 run.py                 # Application entry point
├── 📄 README.md              # Project documentation
└── 📄 LICENSE                # MIT license
```

---

## ✨ Features

- 🌡️ **Simulated Sensor Data** - Real-time temperature sensor simulation
- 📡 **MQTT Communication** - Publisher/Subscriber pattern implementation
- 🖥️ **Interactive CLI** - User-friendly command-line interface
- ⚙️ **Configurable Settings** - Easy broker and topic configuration
- 📝 **Comprehensive Logging** - Connection events and error handling
- 🔄 **Asynchronous Operations** - Non-blocking message handling
- 📁 **Modular Architecture** - Clean, maintainable code structure
- 🚀 **GitHub Ready** - Professional documentation and structure  

---

## Prerequisites

- **Python 3.8+** (with pip)
- **Internet Connection** (for MQTT broker access)
- **Terminal/Command Prompt** access

## 🚀 Quick Start

### 1️⃣ **Clone the Repository**
```bash
git clone https://github.com/kemalerbakirci/MQTT-Fundamentals.git
cd MQTT-Fundamentals
```

### 2️⃣ **Set up Virtual Environment** (Recommended)
```bash
# Create virtual environment
python3 -m venv mqtt_env

# Activate virtual environment
source mqtt_env/bin/activate   # macOS/Linux
# OR
mqtt_env\Scripts\activate       # Windows
```

### 3️⃣ **Install Dependencies**
```bash
pip install -r requirements.txt
```

### 4️⃣ **Run the Application**
```bash
python run.py
```

## ⚙️ Configuration (Optional)

The application works **out of the box** with sensible defaults:
- **MQTT Broker**: `test.mosquitto.org:1883` (public test broker)
- **Topics**: `sensors/temperature` (both publish and subscribe)

### Custom Configuration
If you want to use a different MQTT broker or topics, create a `config/settings.env` file:

```bash
# Create config directory
mkdir config

# Create environment file
cat > config/settings.env << EOF
BROKER_URL=your-broker-url.com
BROKER_PORT=1883
TOPIC_PUB=your/publish/topic
TOPIC_SUB=your/subscribe/topic
EOF
```

> **Note**: Environment files (`.env`) are excluded from version control for security. The application uses default values if no config file is found.

## 🎮 Usage Guide

### Interactive CLI Menu
```
🚀 MQTT Pub/Sub Dashboard
============================
1) Start publishing sensor data
2) View received messages  
3) Exit application
============================
Choose an option (1-3): 
```

#### Menu Options:
| Option | Description | Action |
|--------|-------------|---------|
| **1** | 📤 **Publisher Mode** | Starts publishing simulated temperature data every 2 seconds |
| **2** | 📥 **Subscriber Mode** | Listens for incoming messages and displays them in real-time |
| **3** | 🚪 **Exit** | Safely closes all connections and exits the application |

### Sample Output
**Publisher Mode:**
```json
[PUBLISH] {"timestamp": 1692123456.78, "value": 24.73}
[PUBLISH] {"timestamp": 1692123458.82, "value": 26.41}
```

**Subscriber Mode:**
```json
[MESSAGE] {"timestamp": 1692123456.78, "value": 24.73}
[MESSAGE] {"timestamp": 1692123458.82, "value": 26.41}
```  

---

## � How It Works

### Architecture Overview
```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Publisher     │    │  MQTT Broker    │    │   Subscriber    │
│                 │    │                 │    │                 │
│ Sends sensor    │───▶│ Receives &      │───▶│ Listens &       │
│ data every 2s   │    │ routes messages │    │ displays data   │
│                 │    │                 │    │                 │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

### Technical Details
- **🔄 Asynchronous Operations**: Uses Python threading for non-blocking execution
- **📡 MQTT Protocol**: Lightweight pub/sub messaging for IoT devices
- **📊 JSON Payloads**: Structured data with timestamp and sensor values
- **🌡️ Sensor Simulation**: Generates realistic temperature data (20-30°C range)
- **🔒 Graceful Shutdown**: Handles Ctrl+C interruption cleanly
- **📝 Comprehensive Logging**: Tracks connection status and errors

### Message Flow
1. **Publisher** generates simulated sensor data
2. **JSON payload** is created with timestamp and temperature value
3. **Message published** to MQTT broker on specified topic
4. **Broker distributes** message to all subscribers
5. **Subscriber receives** and displays the real-time data  

---

## � Logging & Monitoring

### Connection Logs
```bash
INFO:app.mqtt_client:Connected to MQTT broker
INFO:app.mqtt_client:Disconnected from MQTT broker (rc=0)
```

### Error Handling
- **Connection failures** are logged with error codes
- **Keyboard interrupts** (Ctrl+C) are handled gracefully
- **Network issues** are automatically managed by paho-mqtt client

## 🚨 Troubleshooting

| Issue | Solution |
|-------|----------|
| `ModuleNotFoundError: paho` | Run `pip install -r requirements.txt` |
| `Connection failed` | Check internet connection and broker URL |
| `Permission denied` | Ensure Python 3.8+ is installed |
| `Port already in use` | Try different MQTT broker port |

## 🎯 Learning Outcomes

After completing this project, you will understand:

- ✅ **MQTT Protocol Basics** - Pub/Sub messaging patterns
- ✅ **IoT Communication** - How devices communicate in real-time
- ✅ **Asynchronous Programming** - Threading and non-blocking operations
- ✅ **Environment Configuration** - Using .env files for settings
- ✅ **Professional Structure** - Modular Python project organization
- ✅ **Error Handling** - Graceful shutdown and exception management

---

## 🤝 Contributing

We welcome contributions! Here's how you can help:

1. **🍴 Fork** the repository
2. **🌿 Create** a feature branch (`git checkout -b feature/amazing-feature`)
3. **💻 Commit** your changes (`git commit -m 'Add amazing feature'`)
4. **📤 Push** to the branch (`git push origin feature/amazing-feature`)
5. **🔄 Open** a Pull Request

### Contribution Ideas
- 🌟 Add more sensor types (humidity, pressure, light)
- 🎨 Improve CLI interface with colors
- 📊 Add data visualization features
- 🔐 Implement authentication for MQTT brokers
- 📱 Create a web dashboard interface

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

```
MIT License - Feel free to use this project for learning and development!
```

## 🙏 Acknowledgments

- **Eclipse Paho** - For the excellent MQTT Python client
- **test.mosquitto.org** - For providing free public MQTT broker
- **Python.org** - For the amazing Python programming language

## 📞 Support

- 🐛 **Found a bug?** [Open an issue](https://github.com/kemalerbakirci/MQTT-Fundamentals/issues)
- 💡 **Have a suggestion?** [Start a discussion](https://github.com/kemalerbakirci/MQTT-Fundamentals/discussions)
- 📧 **Need help?** Check out the [Learning Guide](Learning_Guide_IoT_MQTT.md)

---
<div align="center">

**⭐ Star this repo if you found it helpful! ⭐**

Made with ❤️ for the IoT learning community

</div>

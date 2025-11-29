# MQTT Lab – Mosquitto + Paho  
### Student Name: **Mohammad Sayeh**

---

## 📌 Lab Overview

This lab demonstrates the use of the **MQTT protocol** using:  
- **Mosquitto MQTT Broker**  
- **Paho MQTT Client Library (Python)**  
- **Multiple Publishers (Temperature, Humidity, People Counter)**  
- **Multiple Subscribers (One subscriber per topic)**  

Each publisher sends sensor data periodically to the Mosquitto broker, and each subscriber listens to a specific topic to receive the messages.  
All messages include the student ID as required.

---

## 📁 Folder Structure

```
mqtt_lab/
│
├── temp_publisher.py
├── humidity_publisher.py
├── people_publisher.py
│
├── temp_subscriber.py
├── humidity_subscriber.py
├── people_subscriber.py

```

---

## 🧩 MQTT Topics Used

| Sensor Type        | Topic Name           |
|--------------------|-----------------------|
| Temperature Sensor | `sensor/temperature` |
| Humidity Sensor    | `sensor/humidity`    |
| People Counter     | `sensor/people`      |

---

## 🚀 How the System Works

### ✔️ 1. **Mosquitto Broker**
The broker is installed and running locally on port **1883**:

```
mosquitto -v
```

This broker handles all incoming publisher data and forwards them to the correct subscribers.

---

### ✔️ 2. **Publishers**
Three separate publisher programs were created:

#### 📌 a) Temperature Publisher  
Sends random temperature values:

```python
Temperature: 29.4°C | ID:12218504
```

#### 📌 b) Humidity Publisher  
Sends random humidity values:

```python
Humidity: 61.2% | ID: 12218504
```

#### 📌 c) People Counter Publisher  
Sends random number of detected people:

```python
People Count: 7 | ID: 12218504
```

Each publisher sends a message every **3 seconds**.

---

### ✔️ 3. **Subscribers**
Each subscriber listens for updates on its matching topic:

- `temp_subscriber.py` → listens to `sensor/temperature`
- `humidity_subscriber.py` → listens to `sensor/humidity`
- `people_subscriber.py` → listens to `sensor/people`

Once the publisher sends a message, the subscriber prints it on screen.

---

## 📸 Screenshots (Required for Submission)

### 🔥 Temperature Publisher
<img width="1919" height="1079" alt="Screenshot 2025-11-29 232043" src="https://github.com/user-attachments/assets/51da061c-94eb-4c4e-9386-c16b6841a61f" />


### 🔥 Temperature Subscriber
<img width="1919" height="1079" alt="Screenshot 2025-11-29 232003" src="https://github.com/user-attachments/assets/bf508e6c-0370-4c7f-a8f8-0a02b56cf8fc" />


---

### 💧 Humidity Publisher
<img width="1919" height="1079" alt="Screenshot 2025-11-29 232050" src="https://github.com/user-attachments/assets/f65cc638-ab60-41a2-b79c-08983337d03f" />


### 💧 Humidity Subscriber
<img width="1919" height="1079" alt="Screenshot 2025-11-29 232015" src="https://github.com/user-attachments/assets/96060400-58ac-4549-9102-b2a1b669107e" />


---

### 🧍 People Counter Publisher
<img width="1919" height="1079" alt="Screenshot 2025-11-29 232059" src="https://github.com/user-attachments/assets/40ab397a-1c68-4114-9193-9c0d9d0e562b" />


### 🧍 People Counter Subscriber
<img width="1919" height="1079" alt="Screenshot 2025-11-29 232028" src="https://github.com/user-attachments/assets/bb6816a4-f145-4df5-8cdb-390920e94047" />


---

## 🛠️ How to Run

### 1️⃣ Start Mosquitto Broker
```
mosquitto -v
```

### 2️⃣ Run all Subscribers (3 CMD windows)
```
python temp_subscriber.py
python humidity_subscriber.py
python people_subscriber.py
```

### 3️⃣ Run all Publishers (3 CMD windows)
```
python temp_publisher.py
python humidity_publisher.py
python people_publisher.py
```

You will then see real-time communication happening between publishers and subscribers.

---

## 🏁 Conclusion

This lab demonstrates full MQTT functionality using Mosquitto + Paho in Python.  
All publishers and subscribers work correctly, each message includes the student ID, and results were documented via screenshots.




import paho.mqtt.client as mqtt
import time
import random

BROKER = "localhost"
PORT = 1883
TOPIC = "sensor/humidity"
STUDENT_ID = "12218504"

client = mqtt.Client()
client.connect(BROKER, PORT, 60)

print("Humidity Publisher is running...")

while True:
    hum = round(random.uniform(30.0, 90.0), 2) 
    message = f"Humidity: {hum}% | ID: {STUDENT_ID}"
    client.publish(TOPIC, message)
    print("Sent:", message)
    time.sleep(3)

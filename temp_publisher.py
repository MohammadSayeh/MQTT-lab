import paho.mqtt.client as mqtt
import time
import random

BROKER = "localhost"
PORT = 1883
TOPIC = "sensor/temperature"
STUDENT_ID = "12218504"

client = mqtt.Client()
client.connect(BROKER, PORT, 60)

print("Temperature Publisher is running...")

while True:
    temp = round(random.uniform(20.0, 35.0), 2) 
    message = f"Temperature: {temp}°C | ID: {STUDENT_ID}"
    client.publish(TOPIC, message)
    print("Sent:", message)
    time.sleep(3)  
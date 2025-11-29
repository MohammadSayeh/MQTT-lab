import paho.mqtt.client as mqtt
import time
import random

BROKER = "localhost"
PORT = 1883
TOPIC = "sensor/people"
STUDENT_ID = "12218504"

client = mqtt.Client()
client.connect(BROKER, PORT, 60)

print("People Counter Publisher is running...")

while True:
    count = random.randint(0, 20)  
    message = f"People Count: {count} | ID: {STUDENT_ID}"
    client.publish(TOPIC, message)
    print("Sent:", message)
    time.sleep(3)

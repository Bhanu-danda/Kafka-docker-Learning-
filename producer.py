from kafka import KafkaProducer
import json
import random
import time

producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

cities = ["Hyderabad", "Bangalore", "Mumbai", "Delhi"]

while True:
    order = {
        "order_id": random.randint(1000, 9999),
        "amount": random.randint(100, 5000),
        "city": random.choice(cities)
    }

    producer.send("orders", order)
    print("Sent:", order)

    time.sleep(2)
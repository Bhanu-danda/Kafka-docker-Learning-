from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    "orders",
    bootstrap_servers="kafka:29092",
    auto_offset_reset="earliest",
    group_id="order-consumer-group",
    value_deserializer=lambda x: json.loads(x.decode("utf-8"))
)

print("Consumer started...")

for message in consumer:
    print("Received:", message.value)
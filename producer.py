import random
import time
while True:
    order_id = random.randint(100,999)
    amount = random.randint(500,3000)
    city = random.choice(["Hyderabad","Pune","Benguluru","Mumbai","Vishakapatnam"])

    print(f"order_id={order_id},amount ={amount},city={city}")
    time.sleep(2)
     

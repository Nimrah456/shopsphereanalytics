import random
import time
from faker import Faker

fake = Faker()

def generate_event():
    event_type = random.choice(["order", "click", "session"])
    
    if event_type == "order":
        return {
            "type": "order",
            "order_id": f"ORD{random.randint(1000, 9999)}",
            "user_id": f"USR{random.randint(100, 999)}",
            "product_id": f"P{random.randint(10, 50)}",
            "amount": round(random.uniform(10.0, 500.0), 2),
            "timestamp": fake.iso8601()
        }
    elif event_type == "click":
        return {
            "type": "click",
            "event_id": fake.uuid4()[:8],
            "user_id": f"USR{random.randint(100, 999)}",
            "page": random.choice(["home", "product_detail", "cart", "checkout"]),
            "timestamp": fake.iso8601()
        }
    else:
        return {
            "type": "session",
            "session_id": fake.uuid4()[:8],
            "user_id": f"USR{random.randint(100, 999)}",
            "status": random.choice(["active", "idle", "logged_out"]),
            "timestamp": fake.iso8601()
        }

if __name__ == "__main__":
    for _ in range(5):
        print(generate_event())
        time.sleep(1)
        
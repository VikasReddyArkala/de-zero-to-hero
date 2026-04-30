import json
import csv
from datetime import datetime

orders = [
    {"order_id": "ORD-001", "user_id": 42, "amount": "29.99", "status": "completed", "ts": "2024-03-15 08:23:11"},
    {"order_id": "ORD-002", "user_id": None, "amount": "149.00", "status": "completed", "ts": "2024-03-15 08:45:02"},
    {"order_id": "ORD-003", "user_id": 87, "amount": "29.99",  "status": "COMPLETED", "ts": "2024-03-15 09:01:55"},
    {"order_id": "ORD-004", "user_id": 42, "amount": None,     "status": "refunded",   "ts": "2024-03-15 09:15:30"},
    {"order_id": "ORD-005", "user_id": 99, "amount": "75.50",  "status": "completed",  "ts": "2024-03-15T09:45:00Z"},
    {"order_id": "ORD-002", "user_id": 55, "amount": "149.00", "status": "completed",  "ts": "2024-03-15 08:45:02"},
]

with open("raw_orders.json", "w") as f:
    json.dump(orders, f, indent=2)

print("Raw data written to raw_orders.json")
print(f"Total records: {len(orders)}")
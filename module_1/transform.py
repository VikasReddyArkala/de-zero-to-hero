import json
from datetime import datetime

def transform_orders(raw_orders):
    seen_order_ids = set()
    cleaned = []

    for record in raw_orders:
        record = record.copy()
        # Skip duplicates
        if record["order_id"] in seen_order_ids:
            continue
        seen_order_ids.add(record["order_id"])

        # Normalize status
        record["status"] = record["status"].lower()

        # Parse amount to float
        try:
            record["amount"] = float(record["amount"])
        except (ValueError, TypeError):
            record["amount"] = None

        # Parse timestamp
        try:
            record["ts"] = datetime.strptime(record["ts"], "%Y-%m-%d %H:%M:%S")
        except ValueError:
            try:
                record["ts"] = datetime.strptime(record["ts"], "%Y-%m-%dT%H:%M:%SZ")
            except ValueError:
                record["ts"] = None
        
        # Flag records with missing user_id
        record["missing_user_id"] = record["user_id"] is None

        cleaned.append(record)
    return cleaned

# Load and run
with open("raw_orders.json") as f:
    raw = json.load(f)

result = transform_orders(raw)

print(f"\nRecords after transformation: {len(result)}")
print(f"Records with missing user_id: {sum(1 for r in result if r['missing_user_id'])}")
print(f"Records with null amount: {sum(1 for r in result if r['amount'] is None)}")

total_revenue = sum(r["amount"] for r in result if r["status"] == "completed" and r["amount"] is not None)
print(f"\nTotal revenue from completed orders: ${total_revenue:.2f}")

print("\nFull output:")
for r in result:
    print(r)
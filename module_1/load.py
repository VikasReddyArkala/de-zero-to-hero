import sqlite3
import json
from datetime import datetime
from transform import transform_orders

with open("raw_orders.json") as f:
    raw = json.load(f)

cleaned = transform_orders(raw)

conn = sqlite3.connect("orders.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS orders(
        order_id TEXT PRIMARY KEY,
        user_id INTEGER,
        amount REAL,
        status TEXT,
        ts TEXT,
        missing_user_id INTEGER
    )
""")

for r in cleaned:
    cursor.execute("""
        INSERT OR REPLACE INTO orders (order_id, user_id, amount, status, ts, missing_user_id)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        r["order_id"],
        r["user_id"],
        r["amount"],
        r["status"],
        r["ts"].isoformat() if r["ts"] else None,
        int(r["missing_user_id"])
    ))

conn.commit()
print("Data loaded into orders.db")

# Now query it — just like an analyst would
print("\n--- Total revenue by status ---")
for row in cursor.execute("""
    SELECT status, COUNT(*) as count, ROUND(SUM(amount), 2) as total_revenue
    FROM orders
    GROUP BY status
"""):
    print(row)

print("\n--- Flagged records (missing user_id) ---")
for row in cursor.execute("SELECT * FROM orders WHERE missing_user_id = 1"):
    print(row)

conn.close()
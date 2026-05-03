import pandas as pd
import os
import numpy as np

# Simulate a more realistic dataset — 100,000 orders
np.random.seed(42)
n = 100_000

df_large = pd.DataFrame({
    "order_id": [f"ORD-{i:07d}" for i in range(n)],
    "user_id":  np.random.randint(1, 10000, n),
    "amount":   np.random.uniform(5.0, 500.0, n).round(2),
    "status":   np.random.choice(["completed", "refunded", "pending"], n),
})

df_large.to_csv("orders_large.csv", index=False)
df_large.to_parquet("orders_large.parquet", index=False)

csv_size  = os.path.getsize("orders_large.csv")
parq_size = os.path.getsize("orders_large.parquet")

print(f"CSV size:     {csv_size / 1024:.1f} KB")
print(f"Parquet size: {parq_size / 1024:.1f} KB")
print(f"Parquet is {round(csv_size / parq_size, 1)}x smaller than CSV")

import time

# Read the entire CSV and filter + aggregate
start = time.time()
df_csv = pd.read_csv("orders_large.csv")
total_csv = df_csv[df_csv["status"] == "completed"]["amount"].sum()
csv_time = time.time() - start

# Read only the columns we need from Parquet
start = time.time()
df_parq = pd.read_parquet("orders_large.parquet", columns=["status", "amount"])
total_parq = df_parq[df_parq["status"] == "completed"]["amount"].sum()
parq_time = time.time() - start

print(f"CSV result:     ${total_csv:,.2f}  — took {csv_time:.4f}s")
print(f"Parquet result: ${total_parq:,.2f}  — took {parq_time:.4f}s")
print(f"Parquet was {round(csv_time / parq_time, 1)}x faster")
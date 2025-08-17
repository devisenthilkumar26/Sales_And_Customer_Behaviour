import pandas as pd
import numpy as np
import random

# Number of rows
n_rows = 1000  

# Sample values
customers = [f"C{str(i).zfill(4)}" for i in range(1, 201)]   # 200 customers
products = [f"P{str(i).zfill(3)}" for i in range(1, 51)]     # 50 products
stores = [f"S{str(i).zfill(2)}" for i in range(1, 6)]        # 5 stores
regions = ["North", "South", "East", "West", "Central"]
channels = ["Online", "Offline"]

# Generate dataset
np.random.seed(42)
data = {
    "order_id": [1000 + i for i in range(n_rows)],
    "customer_id": np.random.choice(customers, n_rows),
    "product_id": np.random.choice(products, n_rows),
    "store_id": np.random.choice(stores, n_rows),
    "region": np.random.choice(regions, n_rows),
    "sales_channel": np.random.choice(channels, n_rows),
    "order_date": pd.date_range(start="2023-01-01", periods=n_rows, freq="D"),
    "quantity": np.random.randint(1, 6, n_rows),
    "unit_price": np.random.randint(100, 2000, n_rows),
    "discount": np.round(np.random.choice([0, 0.05, 0.1, 0.15], n_rows), 2)
}

df = pd.DataFrame(data)

# Save to CSV
df.to_csv("data/data_raw/erp_sales_sample.csv", index=False)
print("✅ Generated erp_sales_sample.csv with", n_rows, "rows")

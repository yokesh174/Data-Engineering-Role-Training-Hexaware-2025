import pandas as pd
import numpy as np

# Load dataset (exported from MySQL join of orders + delivery_status)
df = pd.read_csv("orders_delivery.csv")

# Convert date columns
df['order_date'] = pd.to_datetime(df['order_date'], errors='coerce')
df['delivery_date'] = pd.to_datetime(df['delivery_date'], errors='coerce')
df['estimated_date'] = pd.to_datetime(df['estimated_date'], errors='coerce')

# Calculate delay days
df['delay_days'] = (df['delivery_date'] - df['estimated_date']).dt.days

# Mark delayed = 1 if delay_days > 0 else 0
df['delayed'] = np.where(df['delay_days'] > 0, 1, 0)

# Handle missing delivery_date but past estimated_date → delayed
df.loc[df['delivery_date'].isna() & (df['estimated_date'] < pd.Timestamp.today()), 'delayed'] = 1

# Summary of delays by customer
delay_summary = df.groupby('customer_id')['delayed'].sum().sort_values(ascending=False)
print("Top delayed customers:\n", delay_summary.head())

# Save cleaned dataset for reference
df.to_csv("orders_delivery_cleaned.csv", index=False)
print("\nCleaned dataset saved as 'orders_delivery_cleaned.csv'")
# Data Analysis on CSV Files using Pandas

import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# 1. Load CSV File
# -----------------------------
file_path = "sample_sales_data.csv"
df = pd.read_csv(file_path)

print("📌 First 5 rows of the dataset:")
display(df.head())

print("\n📌 Dataset Info:")
print(df.info())

print("\n📌 Summary Statistics:")
display(df.describe())

# -----------------------------
# 2. Total Sales by Product
# -----------------------------
sales_by_product = df.groupby("Product")["Total"].sum()

print("\n📌 Total Sales by Product:")
display(sales_by_product)

plt.figure(figsize=(8,5))
sales_by_product.plot(kind="bar")
plt.title("Total Sales by Product")
plt.xlabel("Product")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.show()

# -----------------------------
# 3. Sales by Category
# -----------------------------
sales_by_category = df.groupby("Category")["Total"].sum()

print("\n📌 Total Sales by Category:")
display(sales_by_category)

plt.figure(figsize=(8,5))
sales_by_category.plot(kind="pie", autopct="%1.1f%%")
plt.title("Sales Distribution by Category")
plt.ylabel("")
plt.tight_layout()
plt.show()

# -----------------------------
# 4. Daily Revenue
# -----------------------------
daily_sales = df.groupby("Date")["Total"].sum()

print("\n📌 Total Sales Per Day:")
display(daily_sales)

plt.figure(figsize=(8,5))
daily_sales.plot(kind="line", marker="o")
plt.title("Daily Sales Trend")
plt.xlabel("Date")
plt.ylabel("Revenue")
plt.grid(True)
plt.tight_layout()
plt.show()

# -----------------------------
# 5. Most Sold Product
# -----------------------------
quantity_by_product = df.groupby("Product")["Quantity"].sum()

print("\n📌 Quantity sold by each product:")
display(quantity_by_product)

plt.figure(figsize=(8,5))
quantity_by_product.plot(kind="bar")
plt.title("Most Sold Product (Quantity)")
plt.xlabel("Product")
plt.ylabel("Units Sold")
plt.tight_layout()
plt.show()

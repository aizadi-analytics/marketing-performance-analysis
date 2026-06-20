This folder contains the Python analysis script for the marketing performance analysis project.
import pandas as pd
import matplotlib.pyplot as plt

# Load data
sales = pd.read_csv("data/sales_daily.csv")
marketing = pd.read_csv("data/marketing_spend.csv")
calendar = pd.read_csv("data/calendar.csv")
channel_mapping = pd.read_csv("data/channel_mapping.csv")

# Inspect data
print("Sales data")
print(sales.head())
print(sales.info())
print(sales.describe())
print(sales.isna().sum())
print("Duplicates:", sales.duplicated().sum())

print("Marketing data")
print(marketing.head())
print(marketing.info())
print(marketing.describe())
print(marketing.isna().sum())
print("Duplicates:", marketing.duplicated().sum())

# Clean date columns
sales["date"] = pd.to_datetime(sales["date"])
marketing["date"] = pd.to_datetime(marketing["date"])
calendar["date"] = pd.to_datetime(calendar["date"])

# Remove duplicate rows
sales = sales.drop_duplicates()
marketing = marketing.drop_duplicates()

# Replace impossible negative values with missing values
sales.loc[sales["orders"] < 0, "orders"] = pd.NA
marketing.loc[marketing["clicks"] < 0, "clicks"] = pd.NA

# Fill missing values using group-level medians
sales["revenue"] = sales.groupby("product_category")["revenue"].transform(
    lambda x: x.fillna(x.median())
)

sales["orders"] = sales.groupby("store")["orders"].transform(
    lambda x: x.fillna(x.median())
)

marketing["spend"] = marketing.groupby("channel")["spend"].transform(
    lambda x: x.fillna(x.median())
)

marketing["clicks"] = marketing.groupby("channel")["clicks"].transform(
    lambda x: x.fillna(x.median())
)

# Final cleaning check
print("Sales missing values after cleaning")
print(sales.isna().sum())

print("Marketing missing values after cleaning")
print(marketing.isna().sum())

print("Sales duplicates after cleaning:", sales.duplicated().sum())
print("Marketing duplicates after cleaning:", marketing.duplicated().sum())

# Business metrics
total_revenue = sales["revenue"].sum()
total_spend = marketing["spend"].sum()
total_orders = sales["orders"].sum()

print("Total revenue:", round(total_revenue, 2))
print("Total marketing spend:", round(total_spend, 2))
print("Total orders:", int(total_orders))

# Average Order Value
sales["aov"] = sales["revenue"] / sales["orders"]

# Daily sales
daily_sales = sales.groupby("date").agg(
    revenue=("revenue", "sum"),
    orders=("orders", "sum")
).reset_index()

# Daily marketing spend
daily_spend = marketing.groupby("date").agg(
    spend=("spend", "sum")
).reset_index()

# Merge daily sales and daily spend
daily = pd.merge(
    daily_sales,
    daily_spend,
    on="date",
    how="left"
)

# ROAS
daily["roas"] = daily["revenue"] / daily["spend"]

print("Daily metrics")
print(daily.head())
print(daily["roas"].describe())

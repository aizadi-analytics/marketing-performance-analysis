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

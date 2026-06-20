# Marketing Performance Analysis

This project analyzes a synthetic marketing and sales dataset using Python and pandas. The goal is to practice a realistic data analysis workflow, including data inspection, cleaning, merging multiple tables, calculating business metrics, visualizing trends, and communicating insights.

## Project goal

The goal of this project is to understand how sales performance, marketing spend, promotions, calendar effects, and marketing channels relate to each other.

The analysis focuses on:

- sales performance by store and product category
- marketing spend by channel
- promotion versus non-promotion days
- weekday versus weekend patterns
- marketing efficiency metrics such as ROAS, CTR, and CPC
- daily and weekly time-series trends

## Dataset

The dataset is synthetic and was created for practice purposes. It contains four tables:

- `sales_daily.csv`: daily sales by date, store, and product category
- `marketing_spend.csv`: daily marketing spend by channel
- `calendar.csv`: calendar features such as weekday, weekend, holiday, week, and month
- `channel_mapping.csv`: metadata about marketing channels, such as channel type and funnel stage

## Tools used

- Python
- pandas
- matplotlib

## Analysis workflow

1. Loaded and inspected the datasets.
2. Checked data types, missing values, duplicates, and invalid values.
3. Cleaned the data by:
   - converting date columns to datetime
   - removing duplicate rows
   - replacing impossible negative values with missing values
   - filling missing values using group-level medians
4. Created business metrics:
   - total revenue
   - total marketing spend
   - total orders
   - AOV
   - ROAS
5. Created marketing efficiency metrics:
   - CTR
   - CPC
6. Used groupby analysis to compare:
   - revenue by store
   - revenue by product category
   - spend by marketing channel
   - promotion versus non-promotion days
   - weekends versus weekdays
7. Created time-series visualizations for daily and weekly trends.

## Figures

The analysis generates visualizations for:

- daily revenue trend
- daily marketing spend trend
- weekly revenue trend

Generated figures are stored in the `figures/` folder.

## Key learning points

- Data cleaning is important before calculating business metrics.
- Group-level medians can preserve more business context than global medians when filling missing values.
- ROAS, CTR, and CPC are useful descriptive metrics, but they do not prove causality.
- Higher revenue during promotion days does not automatically mean the promotion caused all of the increase.
- Sales may also be affected by seasonality, holidays, baseline demand, customer behavior, and other factors.

## Example insights

- Revenue differs by store and product category, so segmentation is important.
- Promotion days show different average revenue and spend compared with non-promotion days, but this should be interpreted as descriptive analysis rather than causal proof.
- Weekly aggregation helps reduce daily noise and makes broader revenue trends easier to interpret.

## Limitations

This is a synthetic practice project and not a production-level Marketing Mix Modelling model. The analysis is descriptive and does not estimate true incrementality. A more advanced analysis would require better causal modelling, control variables, lagged marketing effects, seasonality modelling, and validation on unseen data.

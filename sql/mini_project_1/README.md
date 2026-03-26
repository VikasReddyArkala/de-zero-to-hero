# Mini Project 1 — NYC Taxi SQL Analytics

## Dataset
500,000 synthetic NYC taxi trips generated in PostgreSQL.
Covers full year 2023, six pickup locations, two vendors.

## Queries

| File | Business Question |
|------|------------------|
| q1_monthly_revenue.sql | Monthly revenue summary |
| q2_payment_analysis.sql | Payment type breakdown |
| q3_weekly_revenue_growth.sql | Week-over-week growth |
| q4_high_traffic_locations.sql | High traffic pickup locations |
| q5_most_expensive_trip_per_location.sql | Top trip per location |
| q6_distance_band_analysis.sql | Revenue by distance band |
| q7_location_revenue_ranking.sql | Location performance ranking |
| q8_hourly_demand_patterns.sql | Hourly demand and payment patterns |
| q9_fare_quartile_analysis.sql | Fare distribution quartiles |
| q10_vendor_performance_report.sql | Full vendor comparison report |

## Concepts covered
GROUP BY, HAVING, window functions (ROW_NUMBER, RANK, LAG, NTILE, SUM OVER),
CTEs, conditional aggregation, CASE WHEN, timestamp functions, JOIN between CTEs
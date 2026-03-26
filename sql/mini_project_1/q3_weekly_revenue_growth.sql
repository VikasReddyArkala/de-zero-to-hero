/*
Grain: Per week

Show:
Week starting day: week_start -> DATE_TRUNC('week', pickup_datetime)
total revenue/week: weekly_revenue -> Use CTE to calculate weekly revenue
previous week revenue -> use another cte with lag
percentage change from previous week -> (this week - last week) *100.0 / lastweek
*/

WITH weekly_revenue AS (
    SELECT
        DATE_TRUNC('week', pickup_datetime) as week_start, 
        ROUND(SUM(total_amount)::numeric, 2) AS weekly_revenue
    
    FROM trips
    GROUP BY DATE_TRUNC('week', pickup_datetime)
), 
with_lag AS (
    SELECT 
        week_start, 
        weekly_revenue, 
        LAG(weekly_revenue, 1) OVER (ORDER BY week_start) AS prev_week_revenue
    FROM weekly_revenue
)
SELECT
    week_start::date, 
    weekly_revenue, 
    prev_week_revenue, 
    ROUND(((weekly_revenue - prev_week_revenue) / prev_week_revenue * 100.0 )::numeric, 2) AS pct_change
From with_lag
ORDER BY week_start;
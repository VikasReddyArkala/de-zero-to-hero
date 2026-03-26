/*
Grain - payment type

show no of trips -> trip_count [count(*)]
percentage of total trips -> pct_of_trips
avg tip amount -> avg_tip [avg(tip_amount)]
total revenue -> total_revenue [sum(total_amount)]
*/

WITH payment_stats AS (
    SELECT 
        payment_type, 
        tip_amount, 
        total_amount, 
        COUNT(*) OVER (PARTITION BY payment_type) AS payment_type_count, 
        COUNT(*) OVER() AS total_count
    FROM trips
)

SELECT
    payment_type, 
    COUNT(*) AS trip_count, 
    ROUND((payment_type_count * 100.0 / total_count)::numeric, 2) AS pct_of_trips, 
    ROUND(AVG(tip_amount)::numeric, 2) AS avg_tip, 
    ROUND(SUM(total_amount)::numeric, 2) AS total_revenue

FROM payment_stats
GROUP BY payment_type, payment_type_count, total_count
ORDER BY trip_count DESC

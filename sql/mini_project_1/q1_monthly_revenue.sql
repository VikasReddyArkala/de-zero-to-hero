
SET enable_sort = off;

EXPLAIN ANALYZE
SELECT
    TO_CHAR(pickup_datetime, 'YYYY-MM') AS month, 
    COUNT(*) AS trip_count, 
    ROUND(SUM(total_amount)::numeric, 2) AS total_revenue, 
    ROUND(AVG(fare_amount)::numeric, 2) AS avg_fare, 
    ROUND(AVG(tip_amount)::numeric, 2) AS avg_tip

FROM trips
GROUP BY TO_CHAR(pickup_datetime, 'YYYY-MM')
ORDER BY month;

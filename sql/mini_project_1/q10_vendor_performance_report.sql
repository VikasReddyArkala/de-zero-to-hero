with vendor_stats as (
    select 
        vendor_id, 
        count(*) as total_trips, 
        round(sum(total_amount)::numeric, 2) as total_revenue, 
        round(avg(fare_amount)::numeric, 2) as avg_fare, 
        round(sum(case 
                when payment_type = 'Credit Card' then 1
                else 0
            end) * 100.0 / count(*), 2) as credit_card_rate
    
    from trips
    group by vendor_id
),
vendor_best_location as (
    select 
        vendor_id, 
        pickup_location, 
        round(sum(total_amount)::numeric, 2) as location_revenue, 
        ROW_NUMBER() OVER (
            PARTITION BY vendor_id 
            ORDER BY sum(total_amount) DESC
            ) as rn
    from trips
    group by vendor_id, pickup_location
),
best_location_only AS (
    SELECT vendor_id, pickup_location, location_revenue
    FROM vendor_best_location
    WHERE rn = 1
)

select
    vs.vendor_id, 
    vs.total_trips, 
    vs.total_revenue,
    vs.avg_fare, 
    vs.credit_card_rate, 
    bl.pickup_location as best_location, 
    bl.location_revenue as best_location_revenue, 
    rank() over (order by vs.total_revenue desc) as revenue_rank
from vendor_stats as vs
join best_location_only as bl on vs.vendor_id = bl.vendor_id
order by revenue_rank;
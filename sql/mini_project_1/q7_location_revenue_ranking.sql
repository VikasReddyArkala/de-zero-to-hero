-- CTE for total revenue/location
with total_revenue_per_location as (
    select 
        pickup_location, 
        round(sum(total_amount)::numeric, 2) as total_revenue

    from trips
    group by pickup_location
)

select 
    pickup_location, 
    total_revenue, 
    rank() over (order by total_revenue desc) as revenue_rank, 
    sum(total_revenue) over (order by total_revenue desc) as cumulative_revenue, 
    round(total_revenue * 100.0 / sum(total_revenue) over (), 2) AS pct_of_total

from total_revenue_per_location ;
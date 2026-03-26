with quartile_number as (
    select 
        fare_amount, 
        ntile(4) over (order by fare_amount) as quartile
    from trips
)

select 
    quartile, 
    min(fare_amount) as min_fare, 
    max(fare_amount) as max_fare, 
    round(avg(fare_amount), 2) as avg_fare, 
    count(*) as trip_count

from quartile_number
group by quartile
order by quartile asc;
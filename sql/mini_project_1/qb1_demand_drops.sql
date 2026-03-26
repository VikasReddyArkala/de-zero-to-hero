with hourly_counts as (
    select
        extract (hour from pickup_datetime) as hour,  
        count(*) as trip_count 
        -- round(sum(total_amount)::numeric, 2) as total_revenue

    from trips
    group by extract(hour from pickup_datetime)
    -- order by hour asc 
), 
with_previous as(
    select
        hour, 
        trip_count, 
        lag(trip_count) over (order by hour asc) as prev_hour_count
    
    from hourly_counts
    -- order by hour
)

select 
    hour, 
    trip_count, 
    prev_hour_count,
    (trip_count - prev_hour_count) as drop_count
from with_previous
where trip_count < prev_hour_count 
order by drop_count desc;
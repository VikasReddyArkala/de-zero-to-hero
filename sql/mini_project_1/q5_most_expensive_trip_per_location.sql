/*
Grain: pickup_location/max(total_amount)
pickup_location
dropoff_location
total_amount
trip_distance
payment_type
pickup_datetime

order by total_amount desc
*/

with most_expensive_trip as (
    select 
        pickup_location, 
        total_amount, 
        dropoff_location, 
        trip_distance, 
        payment_type, 
        pickup_datetime, 
        row_number() over (partition by pickup_location order by total_amount desc) as rn
    from trips
)

select 
    pickup_location, 
    dropoff_location, 
    total_amount, 
    trip_distance, 
    payment_type, 
    pickup_datetime

from most_expensive_trip
    where rn = 1
order by total_amount desc;
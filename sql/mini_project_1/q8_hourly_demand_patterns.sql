/*
Grain: no of trips/hour -each day
*/

select 
    extract(hour from pickup_datetime) as hour_of_day, 
    count(*) as trip_count, 
    sum(case 
            when payment_type = 'Credit Card' then 1 
            else 0 
        end) as credit_card_trips, 
    round(sum(case 
                when payment_type = 'Credit Card' then 1 
                else 0 
            end) * 100.0 / count(*), 2
        ) as credit_trip_rate
from trips
group by extract(hour from pickup_datetime)
order by hour_of_day asc;

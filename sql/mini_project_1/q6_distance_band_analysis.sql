/*
Grain: sort by distance

trip_count -> count(*)
average_fare -> avg(fare_amount)
average_tip -> avg(tip_amount)
average furation in min -> avg(trip_duration_mins)

order from shortest to longest
*/
with distance_band_section as (
    select 
        trip_distance, 
        fare_amount, 
        tip_amount, 
        trip_duration_mins, 
        case 
            when trip_distance < 3 then 'Short'
            when trip_distance between 3 and 10 then 'Medium'
            when trip_distance between 10 and 20 then 'Long'
            else 'Very Long'
        end as distance_band
    
    from trips
)

select 
    distance_band, 
    count(*) as trip_count, 
    round(avg(fare_amount)::numeric, 2) as avg_fare, 
    round(avg(tip_amount)::numeric, 2) as avg_tip, 
    round(avg(trip_duration_mins)::numeric, 2) as avg_trip_duration

from distance_band_section
group by distance_band
order by case distance_band 
    when 'Short' then 1
    when 'Medium' then 2
    when 'Long' then 3
    when 'Very Long' then 4
end;
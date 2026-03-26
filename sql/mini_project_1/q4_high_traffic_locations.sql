/*
Grain:pickup_location with min 90000 pickups and avg distance of 5
show
location name -> pickup_location > 90,000 pickups and avg(trip_distance) > 5
trip count -> count(*)
average distance -> AVG(trip_distance)
average fare -> AVG(fare_amount)

order by trip_count DESC
*/

select 
    pickup_location,
    count(*) as trip_count, 
    round(avg(trip_distance)::numeric, 2) as avg_distance,
    round(avg(fare_amount)::numeric, 2) as avg_fare

from trips
group by pickup_location
having count(*) > 83000 and avg(trip_distance) > 12.7
order by trip_count desc;